package com.springboot.app.my.first.app;

import java.util.List;

import java.util.ArrayList;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class StudentController {
	//HTTP://localhost:8080/student
	
     @GetMapping("/student")
	public Student getStudent() {
		return new Student("Erastus", "Kemboi");
		
	}
     @GetMapping("/students")
     public List<Student> getStudents(){
    	 List<Student> students = new ArrayList<>();
    	 students.add(new Student("Erastus", "Kemboi"));
    	 students.add(new Student("Delvis", "mutai"));
    	 students.add(new Student("Anthony", "Kipkemoi"));
    	 students.add(new Student("Judy", "Jepkoech"));
    	 return students;
     }
     //http://locahost:8080/student/erastus/kemboi
     //@PathVariable annotation
         @GetMapping("/student/{firstName}/{lastName}")
    	 public Student studentPathvariable(@PathVariable("firstName")String firstName, @PathVariable("lastName")String lastName) {
    	 return new Student(firstName, lastName);
     }
         //build rest API to handle query parameters
         //http:localhost:8080/student?firstname=Erastus
         
         @GetMapping("/query")
         public Student getRequestParam(@RequestParam(name= "firstName")String firstName,@RequestParam(name="lastName") String lastName) {
        	 return new Student(firstName,lastName);
         }
    	 
}
