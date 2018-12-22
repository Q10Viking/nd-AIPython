def create_cast_list(filename):
    cast_list = []
    #use with to open the file filename
    with open(filename,'r') as f:
        #use the for loop syntax to process each line
        for line in f:
            #and add the actor name to cast_list
            cast_list.append(line.split(',')[0])


    return cast_list

cast_list = create_cast_list('flying_circus_cast.txt')
for actor in cast_list:
    print(actor)

'''
Graham Chapman
Eric Idle
Terry Jones
Michael Palin
Terry Gilliam
John Cleese
Carol Cleveland
Ian Davidson
John Hughman
The Fred Tomlinson Singers
Connie Booth
Bob Raymond
Lyn Ashley
Rita Davies
Stanley Mason
David Ballantyne
Donna Reading
Peter Brett
Maureen Flanagan
Katya Wyeth
Frank Lester
Neil Innes
Dick Vosburgh
Sandra Richards
Julia Breck
Nicki Howorth
Jimmy Hill
Barry Cryer
Jeannette Wild
Marjorie Wilde
Marie Anderson
Caron Gardner
Nosher Powell
Carolae Donoghue
Vincent Wong
Helena Clayton
Nigel Jones
Roy Gunson
Daphne Davey
Stenson Falke
Alexander Curry
Frank Williams
Ralph Wood
Rosalind Bailey
Marion Mould
Sheila Sands
Richard Baker
Douglas Adams
Ewa Aulin
Reginald Bosanquet
Barbara Lindley
Roy Brent
Jonas Card
Tony Christopher
Beulah Hughes
Peter Kodak
Lulu
Jay Neill
Graham Skidmore
Ringo Starr
Fred Tomlinson
David Hamilton
Suzy Mandel
Peter Woods
'''