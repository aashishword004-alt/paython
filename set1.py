# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


amit_skills = {"Python", "Java", "SQL", "Git", "Linux"}

rahul_skills = {"Python", "C++", "SQL", "Git"}

priya_skills = {"Python", "Java", "SQL", "Machine Learning"}


#{machine learning , c++ , linux}
all_skills = amit_skills | rahul_skills | priya_skills

unique_skills = {
    skill for skill in all_skills
   if sum(skill in s for s in [amit_skills, rahul_skills, priya_skills]) == 1
}

print(unique_skills)


# output = {machinlearning ,c++,git,linux}
