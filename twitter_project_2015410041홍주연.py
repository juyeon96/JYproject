#-*- coding: utf-8 -*-

import codecs

u = codecs.open("user.txt", "r", "utf-8") #store user info
userlines = [line[:-1] for line in u]
id_num = [0 for i in range(int(len(userlines)/4))]
signup = [0 for i in range(int(len(userlines)/4))]
account = [0 for i in range(int(len(userlines)/4))]
for i in range(int(len(userlines)/4)):
    id_num[i] = userlines[i*4]
    signup[i] = userlines[i*4+1]
    account[i] = userlines[i*4+2]
print ("Scanned user info...")

f = codecs.open("friend.txt", "r", "utf-8") #store friendship info
friendlines = [line[:-1] for line in f]
friend = [["" for col in range(len(friendlines))] for row in range(len(id_num))]
fcount = [0 for i in range(len(id_num))]
for i in range(int((len(friendlines)/3))):
    userid = friendlines[i*3]
    for j in range(len(id_num)):
        if id_num[j] == userid:
            fcount[j] = fcount[j]+1
            kk = j
            break
    for j in range(len(friendlines)):
        if friend[kk][j] == "":
            friend[kk][j] = friendlines[i*3+1]
            break
print ("Scanned friendship info...")

t = codecs.open("word.txt", "r", "utf-8") #store tweets
tweetlines = [line[:-1] for line in t]
tweet = [["" for col in range(len(tweetlines))] for row in range(len(id_num))]
tcount = [0 for i in range(len(id_num))] #store how many words each person tweeted
onlyword = [0 for i in range(int(len(tweetlines)/4))] #store words in array
for i in range(int(len(tweetlines)/4)):
    userid = tweetlines[i*4]
    onlyword[i] = tweetlines[i*4+2]
    for j in range(len(id_num)):
        if id_num[j] == userid:
            tcount[j] = tcount[j]+1
            kkk = j
            break
    for j in range(len(tweetlines)):
        if tweet[kkk][j] == "":
            tweet[kkk][j]= tweetlines[i*4+2]
            break
print ("Scanned tweets...")

fmin = fcount[0] #find min, max friend num
fmax = fcount[0]
def friendcount():
    global fmin
    global fmax
    for i in range(len(fcount)):
        if fcount[i]<fmin and fcount[i]>=0:
            fmin = fcount[i]
        if fcount[i]>fmax:
            fmax = fcount[i]

tmin = tcount[0] #find min, max tweet num
tmin_i = 0
tmax = tcount[0]
tmax_i = 0
def tweetcount():
    global tmin
    global tmin_i
    global tmax
    global tmax_i
    for i in range(len(tcount)):
        if tcount[i]<tmin and tcount[i]>=0:
            tmin = tcount[i]
            tmin_i = i
        if tcount[i]>tmax:
            tmax = tcount[i]
            tmax_i = i #store index of tmax to use it in menu 3

class Vertex:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}

    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])

    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight

    def get_connections(self):
        return self.adjacent.keys()  

    def get_id(self):
        return self.id

    def get_weight(self, neighbor):
        return self.adjacent[neighbor]

class Graph:
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.vert_dict.values())

    def add_vertex(self, node):
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(node)
        self.vert_dict[node] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None

    def add_edge(self, frm, to, cost = 0):
        if frm not in self.vert_dict:
            self.add_vertex(frm)
        if to not in self.vert_dict:
            self.add_vertex(to)

        self.vert_dict[frm].add_neighbor(self.vert_dict[to], cost)
        self.vert_dict[to].add_neighbor(self.vert_dict[frm], cost)

    def get_vertices(self):
        return self.vert_dict.keys()

while True:
    select = input("0. Read data files\n1. display statistics\n2. Top 5 most tweeted words\n3. Top 5 most tweeted users\n4. Find users who tweeted a word\n5. Find all people who are friends of the above users\n6. Delete all mentions of a word\n7. Delete all users who mentioned a word\n8. Find strongly connected components\n9. Find shortest path from a given user\n99. Quit\nSelect Menu: ")

    if select!="0" and select!="1" and select!="2" and select!="3" and select!="4" and select!="5" and select!="6" and select!="7" and select!="8" and select!="9" and select!="99":
        while True:
            select = input("Choose a right number: ")
            if select=="0" or select=="1" or select=="2" or select=="3" or select=="4" or select=="5" or select=="6" or select=="7" or select=="8" or select=="9" or select=="99":
                break

    if select == "0":
        totaluser = len(userlines)/4
        print ("Total users: %s" % (int(len(userlines)/4)))
        print ("Total friendships records: %s" % (int(len(friendlines)/3)))
        print ("Total tweets: %s" % (int(len(tweetlines)/4)))

    elif select == "1":
        friendcount()
        fa = (len(friendlines)/3)/len(id_num)
        print ("Average number of friends: %s" % (fa))
        print ("Minimum friends: %s" % (fmin))
        print ("Maximum number of friends: %s" % (fmax))

        tweetcount()
        ta = (len(tweetlines)/4)/len(id_num)
        print ("Average tweets per user: %s" % (ta))
        print ("Minimum tweets per user: %s" % (tmin))
        print ("Maximum tweets per user: %s" % (tmax))
    elif select == "2": #too much running time
        tcount_word = [1 for i in range(len(onlyword))]
        for i in range(len(onlyword)):
            if i>0:
                for j in range(len(onlyword)):
                    if onlyword[j] == onlyword[i]:
                        tcount_word[i] = tcount_word[i]+1
                        tcount_word[j] = -10
                        break
        wmin = tcount_word[0]
        wm = 0
        for i in range(len(tcount_word)):
            if tcount_word[i] < wmin and tcount_word > 0:
                wmin = tcount_word[i]
                wm = i #index of least tweeted word
        wtop1 = tcount_word[0]
        w1 = 0
        for i in range(len(tcount_word)):
            if tcount_word[i] > wtop1:
                wtop1 = tcount_word[i]
                w1 = i #index of most tweeted word
        wtop2 = wmin
        w2 = wm
        for i in range(len(tcount_word)):
            if tcount_word[i] > wtop2 and tcount_word[i] < wtop1:
                wtop2 = tcount_word[i]
                w2 = i #index of second most tweeted word
        wtop3 = wmin
        w3 = wm
        for i in range(len(tcount_word)):
            if tcount_word[i] > wtop3 and tcount_word[i] < wtop2:
                wtop3 = tcount_word[i]
                w3 = i #index of third most tweeted word
        wtop4 = wmin2
        w4 = wm
        for i in range(len(tcount_word)):
            if tcount_word[i] > wtop4 and tcount_word[i] < wtop3:
                wtop4 = tcount_word[i]
                w4 = i #index of fourth most tweeted word
        wtop5 = wmin
        w5 = wm
        for i in range(len(tcount_word)):
            if tcount_word[i] > wtop5 and tcount_word[i] < wtop4:
                wtop5 = tcount_word[i]
                w5 = i #index of fifth most tweeted word

        print ("1. %s" % (onlyword[w1]), end="")

        if w1 != w2:
            print ("2. %s" % (onlyword[w2]), end="")
        if w2 != w3:
            print ("3. %s" % (onlyword[w3]), end="")
        if w3 != w4:
            print ("4. %s" % (onlyword[w4]), end="")
        if w4 != w5:
            print ("5. %s" % (onlyword[w5]), end="")

    elif select == "3":
        tweetcount()
        umin = tmin
        um = tmin_i
        utop1 = tmax
        u1 = tmax_i
        utop2 = umin
        u2 = um
        for i in range(len(tcount)):
            if tcount[i] > utop2 and tcount[i] < utop1:
                utop2 = tcount[i]
                u2 = i
        utop3 = umin
        u3 = um
        for i in range(len(tcount)):
            if tcount[i] > utop3 and tcount[i] < utop2:
                utop3 = tcount[i]
                u3 = i
        utop4 = umin
        u4 = um
        for i in range(len(tcount)):
            if tcount[i] > utop4 and tcount[i] < utop3:
                utop4 = tcount[i]
                u4 = i
        utop5 = umin
        u5 = um
        for i in range(len(tcount)):
            if tcount[i] > utop5 and tcount[i] < utop4:
                utop5 = tcount[i]
                u5 = i

        print ("1.\n%s%s%s\n" % (id_num[u1], signup[u1], account[u1]))
        if u1 != u2:
            print ("2.\n%s\n%s\n%s\n" % (id_num[u2], signup[u2], account[u2]))
        if u2 != u3:
            print ("3.\n%s\n%s\n%s\n" % (id_num[u3], signup[u3], account[u3]))
        if u3 != u4:
            print ("4.\n%s\n%s\n%s\n" % (id_num[u4], signup[u4], account[u4]))
        if u4 != u5:
            print ("5.\n%s\n%s\n%s\n" % (id_num[u5], signup[u5], account[u5]))
    elif select == "4":
        word = input("Write a word to find: ")
        
        o = 0
        while True: #if o is 0, quit while, if o is 1, keep doing while
            for i in range(len(word)):
                if word[i] == " ":
                    o = 1
                    break
                else:
                    o = 0
            if o == 0:
                break
        
        finduser = [0 for i in range(len(id_num))]
        usernum = 1
        wordindex = 0
        for i in range(len(onlyword)):
            if onlyword[i] == word:
                wordindex = i

        for i in range(len(id_num)):
            for j in range(len(tweetlines)):
                if tweet[i][j] == word:
                    finduser[i] = 1
                    print ("%s.\n%s\n%s\n%s" % (usernum, id_num[i], signup[i], account[i]))
                    usernum = usernum+1
                    break
        while True:
            select_two = input("5. Find all people who are friends of the above users\n6. Delete all mentions of a word\n7. Delete all users who mentioned a word\n99. Show all menu\nSelect Menu: ")

            if select_two!="5" and select_two!="6" and select_two!="7" and select_two!="99":
                while True:
                    select_two = input("Choose a right number: ")
                    if select_two=="5" or select_two=="6" or select_two=="7" or select_two=="99":
                        break

            if select_two == "5":
                for i in range(len(id_num)):
                    if finduser[i] == 1:
                        friendnum = 1
                        print ("Find friend of %s..." % (id_num[i]))
                        for j in range(len(friendlines)):
                            if friend[i][j] != "":
                                print ("%s.\n%s" % (friendnum, friend[i][j]))
                                friendnum = friendnum+1
            elif select_two == "6":
                count6 = 0
                tindex1 = [0 for i in range(int(len(tweetlines)/4))]
                for i in range(int(len(tweetlines)/4)):
                    if tweetlines[i*4+2] == word:
                        tindex1[i] = 1
                for i in range(len(tindex1)):
                    if tindex1[i] == 1:
                        tweetlines.pop((i-count6)*4)
                        tweetlines.pop((i-count6)*4+1)
                        tweetlines.pop((i-count6)*4+2)
                        tweetlines.pop((i-count6)*4+3)
                        count6 = count6+1
                for i in range(len(onlyword)):
                    if onlyword[i] == word:
                        onlyword.pop(i)
                        break
                tindex2 = [[0 for col in range(len(tweetlines))] for row in range(len(id_num))]
                for i in range(len(id_num)):
                    for j in range(len(tweetlines)):
                        if tweet[i][j] == word:
                            tcount[i] = tcount[i]-1
                            tindex2[i][j] = 1
                    for j in range(len(tweetlines)):
                        if tindex2[i][j] == 1:
                            tweet[i][j] = ""
            elif select_two == "7":
                count7=0
                uindex = [0 for i in range(len(id_num))]
                for i in range(len(id_num)):
                    for j in range(len(tweetlines)):
                        if tweet[i][j] == word:
                            id_num.pop(i-count7)
                            signup.pop(i-count7)
                            account.pop(i-count7)
                            userlines.pop((i-count7)*4)
                            userlines.pop((i-count7)*4+1)
                            userlines.pop((i-count7)*4+2)
                            userlines.pop((i-count7)*4+3)
                            count7 = count7+1 #use count to avoid index out of range
                            break
            elif select_two == "99":
                break
    elif select == "5" or select == "6" or select == "7":
        print ("You should do 4 first to do this function")
    elif select == "8":
        print ("Strongly connected components")
    elif select == "9":
        username = input("Write an identification number of a user: ")
        print ("Finding shortest path from a given user...")
    elif select == "99":
        break
