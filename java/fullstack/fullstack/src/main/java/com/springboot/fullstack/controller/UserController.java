package com.springboot.fullstack.controller;

import com.springboot.fullstack.model.User;
import com.springboot.fullstack.repository.UserRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.PatchMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class UserController {
      @Autowired
      private UserRepository userRepository;

      @PostMapping("/user")
      User newUser(@RequestBody User newUser){
          return userRepository.save(newUser);
      }

}
