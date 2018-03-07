#Kamaaria Sanders 
#University of Michigan
#Tembo Code Challenge


parents = [
    {'parent': 'Henry', 'child': {'name': 'Calvin', 'age': 2}},
    {'parent': 'Ada', 'child': {'name': 'Lily', 'age': 3}},
    {'parent': 'Emilia', 'child': {'name': 'Petra', 'age': 1}},
    {'parent': 'Biff', 'child': {'name': 'Biff Jr', 'age': 4}},
    {'parent': 'Milo', 'child': {}}
]

curriculum = [
    {
        'age': 1,
        'activity': [
            'Try singing a song together.',
            'Point and name objects.'
            ]
    },
    {
        'age': 2,
        'activity': [
            'Go outside and feel surfaces.',
            'Draw with crayons.',
            'Play with soundmaking toys or instruments.',
            'Look at family pictures together.'
            ]
    },
    {
        'age': 3,
        'activity': [
            'Build with blocks.',
            'Try a simple puzzle.',
            'Read a story together.'
            ]
    }
]

count = 0
while count < len(parents):
    parentname = parents[count].get('parent')
    if parents[count].get('child') != {}:
        childname = parents[count].get('child').get('name')
        childage = parents[count].get('child').get('age')

        if childage >= 1 and childage <= 3:
            print 'Hello ' + parentname + ', here are some activities to do with your ' + str(childage) + ' year old child ' + childname

            activityCount = 0
            while activityCount < len(curriculum[childage - 1].get('activity')):
                numActivities = len(curriculum[childage - 1].get('activity'))
                activityCount = 0
                while activityCount < numActivities:
                    print(curriculum[int(childage) - 1].get('activity')[activityCount])
                    activityCount = activityCount + 1
                activityCount = activityCount + 1
        else:
            print 'Hello '+ parentname + ', there are no activities for your '+ str(childage) + ' year old child '+ childname
    else:
        print 'Hello ' + parentname + ', you need to enter your childs name and age!'
    print'curriculum complete!\n'
    count = count + 1



