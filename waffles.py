like_waffles = input("Do you like waffles?")

if likes_waffles == 'yes':
    print ("yeah we like waffles!")
    likes_pancakes = input("do you like pancakes")
    if likes_pancakes == 'yes':
        print("yeah we like pancakes")
        likes_french_toast = input("do you like french toast")
        if likes_french_toast == 'yes':
         print("yeah we like pancakes")
        else:
             print("french toast is BOSS")
    else:
        print("well we like pancakes")
else:
    print("well we like waffles")
    
