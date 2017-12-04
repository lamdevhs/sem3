
import Data.Array

class Hashable a where
    hash :: a -> Integer

data HashT key value = HashT {
    content :: Array Int (Maybe (HashTElem key value)),
    hashf :: key -> Int }

data HashTElem key value = HashTElem key value Bool deriving Show

mkHashT :: Hashable key => Int -> HashT key value
mkHashT size = HashT {content = a, hashf = f }
  where
    a = array (0,size - 1) (replicate size Nothing)
    f x = hash x % size

modHashT
  :: HashT key value
  -> [(Int, Maybe (HashTElem key value))]
  -> HashT key value
modHashT ht@(HashT arr _) newElems = ht { content = arr // newElems }

nextEmptyCell :: HashT key value -> key -> Maybe Int
nextEmptyCell ht k = asum (fmap f toTest)
  where
    maxIx= snd (bounds $ content ht)
    kIx = hashf ht k
    indexes = [kIx..maxIx - 1] ++ [0..kIx - 1]
    toTest = [(ix, a ! ix) | ix <- indexes]
    f (ix, Nothing) = Just ix
    f (ix, Just (HashTElem _ _ True)) = Just ix
    f (ix, _) = Nothing

indexByKey :: HashT key value -> key -> Maybe Int
indexByKey ht key = asum (fmap f toTest)
  where
    maxIx = snd (bounds $ content ht)
    kIx = hashf ht k
    indexes = [kIx..maxIx - 1] ++ [0..kIx - 1]
    toTest = [(ix, a ! ix) | ix <- indexes, not isNothing (a ! ix) ]
    f (ix, Just (HashTElem _ _ True)) = Nothing
    f (ix, Just (HashTElem key _ False)) = when (key' == key) (pure ix)

add :: HashT key value -> (key, value) -> HashT key value
add ht (k, v)
  | k `keyOf` ht = error "Key already exists"
  | otherwise    = modHashT ht [newElem]
      where
        ix = hashf ht k
        newElem = (ix, Just (k, v))

keyOf :: key -> HashT key value -> Bool
k `keyOf` ht =
    case arr ! ix of
      Nothing -> False
      Just (k', v) -> k' == k
  where
    ix = hashf ht k
    arr = content ht

delete :: HashT key value -> key -> HashT key value
delete ht key = modHashT ht [(ix, Nothing)]
  where
    ix = hashf ht key

lookup :: HashT key value -> key -> HashT key value
lookup ht key =
    maybe (get ht key) (error "Key not found") getValue
  where
    getValue = snd

get :: HashT key value -> key -> Maybe (key, value)
get ht key = (arr ! ix) >>= must (\(key', value) -> key' == key)
  where
    arr = content ht
    ix = hashf ht key

must :: MonadPlus m => (a -> Bool) -> a -> m a
must test a = if test a then pure a else mzero

instance (Show key, Show value) => Show (HashT key value) where
  show ht = toList (content ht) & fmap f & lines
    where
      f (ix, maybePair) = show ix ++ " - " ++ rest
        where rest = maybe "" show maybePair
