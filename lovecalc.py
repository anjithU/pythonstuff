def calculate_love_score(name1,name2):
    
    combined_name = name1.lower()+name2.lower()

    t = combined_name.count("t")
    r = combined_name.count("r")
    u = combined_name.count("u")
    e = combined_name.count("e")
    
    l = combined_name.count("l")
    o = combined_name.count("o")
    v = combined_name.count("v")
    e = combined_name.count("e")
    print(f"your love score is {t+r+u+e} {l+o+v+e}")

    print(combined_name)



calculate_love_score("Anjith","Mathew")