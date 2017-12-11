package CtrlTower;

import java.util.PriorityQueue;
import java.util.Queue;
import java.util.Timer;
import java.util.TimerTask;
import java.util.concurrent.ConcurrentLinkedDeque;


public class ControlTower {

	public static final int DELAI_REPONSE_TOUR_MS = 4000;
	public static final int INTERVALLE_MS = 1000;
	
	public PriorityQueue<Vol> fileAttente = new PriorityQueue<Vol>();
	
	public ControlTower() {
		
		Timer avionsTimer = new Timer();
		avionsTimer.scheduleAtFixedRate(
				new NouvelAvion(this),
				0,
				ControlTower.INTERVALLE_MS);
		
		Timer tourTimer = new Timer();
		tourTimer.scheduleAtFixedRate(
				new DécisionTour(this),
				ControlTower.DELAI_REPONSE_TOUR_MS,
				ControlTower.INTERVALLE_MS);
	}

	public class NouvelAvion extends TimerTask {

		ControlTower tour;
		
		public NouvelAvion(ControlTower tc) {
			this.tour = tc;
		}
		
		@Override
		public void run() {
			this.tour.fileAttente.add(new Vol());
		}
	}
	
	public class DécisionTour extends TimerTask {

		ControlTower tour;
		
		public DécisionTour(ControlTower tc) {
			this.tour = tc;
		}
		
		@Override
		public void run() {
			Vol v = this.tour.fileAttente.peek();
			v.atterrir();
			this.tour.fileAttente.remove();
			System.out.println(this.tour);
		}
	}

	public String toString() {
		return this.fileAttente.toString();
	}
	
	public static void main(String args[]) {
		new ControlTower();
	}
	
	
}
