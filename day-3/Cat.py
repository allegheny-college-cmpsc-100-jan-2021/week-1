#!/usr/bin/env python

class Cat:
    
    def __init__(self, name: str, fur_color: str, is_tabby: bool):
        """Creates basic properties for a cat
        
        Keyword arguments:
        name -- Name of the cat
        fur_color -- Cat's fur color
        is_tabby -- Boolean representing if the cat is a tabby cat or not
        """
        self.name = name
        self.fur_color = fur_color
        self.is_tabby = is_tabby
        
    def __str__(self):
        """Returns a standard string for object when printed"""
        tabby = "tabby" if self.is_tabby else "non-tabby"
        return f"{self.name} is a {self.fur_color} {tabby} cat." 
    
    def is_friends_with(self, cat):
        """Determines if two cats are friends based on rules
        
        Keyword arguments: 
        cat -- cat object to compare
        """
        # TODO: Complete this method to see if the cat parameter
        #       satisfies the criteria to be friends with Ulysses
        #       return boolean True if yes, boolean False if not