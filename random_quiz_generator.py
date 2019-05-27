import random

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
   'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
   'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
   'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
   'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
   'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
   'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
   'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
   'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
   'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
   'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
   'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
   'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
   'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
   'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

for q in range(35):
    qFile = open('captialQuizQ%s.txt'%(q + 1), 'w')
    resFile = open('capitalQuizA%s.txt'%(q + 1), 'w')
    qFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    qFile.write('State Capitals Quiz(Form %s)' % (q + 1))
    qFile.write('\n\n')
    states = list(capitals.keys())
    random.shuffle(states)

    for qN in range(50):
        cres = capitals[states[qN]]
        wres = list(capitals.values())
        del wres[wres.index(cres)]
        wres = random.sample(wres, 3)
        ansOpt = wres + [cres]
        random.shuffle(ansOpt)
        qFile.write('%s. What is the capital of %s?\n' % (qN + 1, states[qN]))
        for i in range(4):
            qFile.write('    %s. %s\n' % ('ABCD'[i], ansOpt[i]))
        qFile.write('\n')
        resFile.write('%s. %s\n' % (qN + 1, 'ABCD'[ansOpt.index(cres)]))
    qFile.close()
    resFile.close()
