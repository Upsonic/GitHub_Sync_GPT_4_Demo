def create_data(file):
  with open(file, "w") as f:
    f.write("""
age,height,weight,gender
25,180,80,male
30,175,68,female
22,170,70,male
25,180,75,male
33,170,68,female
45,185,85,male
55,175,80,female
24,182,76,male
35,168,65,female
40,178,70,male
50,166,62,female
28,175,68,male
32,172,72,female
21,185,85,male
29,170,65,female
41,182,73,male
43,175,70,female
37,180,77,male
36,164,60,female
25,180,75,male
33,170,68,female
45,185,85,male
55,175,80,female
24,182,76,male
35,168,65,female
40,178,70,male
50,166,62,female
28,175,68,male
32,172,72,female
21,185,85,male
29,170,65,female
41,182,73,male
43,175,70,female
37,180,77,male
36,164,60,female
""")
