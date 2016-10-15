from User import User
from Friends import Friends
import datetime

user = User('reigning')
UserId = user.execute()
friends = Friends(UserId)
friends.execute()

friends.hist1()
friends.hist2()
