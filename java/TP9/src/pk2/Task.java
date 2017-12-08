package pk2;

import java.util.ArrayList;
import java.util.Collections;

public class Task implements Comparable {

	int priority;
	String label;
	Task(String l, int p) {
		this.priority = 1;
		if (p >= 1 && p <= 1000) this.priority = p;
		this.label = l;
	}
	
	@Override
	public int compareTo(Object arg0) {
		Task other = ((Task) arg0);
		int diff = other.priority - this.priority;
		if (diff == 0) {
			return this.label.compareTo(other.label);
		}
		return diff;
	}
	
	public String toString() {
		return "Task (" +
				String.valueOf(this.priority)
		       + "," + this.label + ")";
	}
	
	public static void main(String[] args) {
		ArrayList<Task> taskList = new ArrayList<Task>();
		taskList.add(new Task("Study some maths", 150));
		taskList.add(new Task("Order takeout", 80));
		taskList.add(new Task("Learn Java", 100));
		taskList.add(new Task("Chill/watch some movie", 50));
		taskList.add(new Task("Get some sleep", 80));
		Collections.sort(taskList);
		System.out.println(taskList);
	}

}
