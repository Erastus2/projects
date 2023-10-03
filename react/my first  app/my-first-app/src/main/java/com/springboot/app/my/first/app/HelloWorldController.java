package com.springboot.app.my.first.app;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class HelloWorldController {
	//get HTTP method
	//http://locahost:8080/hello
	@GetMapping("/hello")
	public String helloWorld() {
		return "Hello Erastus";
	}
 
}
