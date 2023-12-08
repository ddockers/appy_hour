import datetime

# Create some sort of logic where at a particular time of the way/week, a venue will be given with the happy hour deal(s) on offer

now = datetime.datetime.now()

'''
Solution 1
User input day.
Output = venue, offer and time
'''

'''
Solution 2
now = datetime.datetime.now()
When now = true, output venue, offer and time
'''

'''
Box Bar 241 Sun-Thurs all day
The Smithfield Social 2 4 £12 Mon-Fri 1600-1900
Foundry Project 2 4 £10 Sun-Thurs 1500-2100
Pixel Bar 241 everyday
7Sins 2 4 £10 everyday until 7pm
Bee House 2 4 £8 all day
Clubhouse 2 4 £12 12pm-6pm Sun-Mon & Wed-Fri
Las Iguanas 241 all day everyday
Federal 2 4 £12 ADED
Lonocove (NQ) £6 Mon-Thurs & Fri-Sat ubtil 8pm
Be at one 241
Onn Bar 241 Tues
The Blues Kitchen £6 Weds
The Drop (Chorlton) 241 9pm-is
Point Blank
Motley 241 Mon-Fri 5-8
Revs sun-fri all day 2 4 £10
Oxnoble (Liverpool rd) 241 ADED
On the Hush 241 all day Wed, 1700-x Thu/Fri, 2000-x Sat, 1500-x Sun
Banyan Tree (Castlefield) 2 cocktails for £12 & 2 house dbls for £10, Mon 1730-1930, Tue-Sat 1900-2100, Sun 1600-2000
Barca 241 12pm-x Tues-Fri
Turtle Bay Sun-Fri 1100-1900 & 2130-2330/0130. Sat 1000-1900 & 2130-0130
Tiki Hideaway NQ 2 for £14 until 2100
The Shack NQ 2 for £12 Mon-Fri 1600-1900
Blockbuster NQ 2 for £10 until 2000
Dirty Martini 50% off cocktails Mon-Fri until 2100, Sat until 1900, Sun all day
Guilty by Association NQ 2 for £12 Sun-Fri until 2200, Sat until 2100
'''

happy_hour_offers = {
    'Box Bar (Deansgate)' : [
        {'day' : 'Sunday', 'start_time' : '11:00', 'end_time' : '23:59', 'offer' : '2 for 1 cocktails'},
        {'day' : 'Monday', 'start_time' : '12:00', 'end_time' : '23:59', 'offer' : '2 for 1 cocktails'},
        {'day' : 'Tuesday', 'start_time' : '12:00', 'end_time' : '23:59', 'offer' : '2 for 1 cocktails'},
        {'day' : 'Wednesday', 'start_time' : '12:00', 'end_time' : '23:59', 'offer' : '2 for 1 cocktails'},
     
    ],
    'The Smithfield Social' : [
        {'day' : 'Monday', 'start_time' : '16:00', 'end_time' : '19:00', 'offer' : '2 cocktails for £12'},
        {'day' : 'Tuesday', 'start_time' : '16:00', 'end_time' : '19:00', 'offer' : '2 cocktails for £12'},
        {'day' : 'Wednesday', 'start_time' : '16:00', 'end_time' : '19:00', 'offer' : '2 cocktails for £12'},
        {'day' : 'Thursday', 'start_time' : '16:00', 'end_time' : '19:00', 'offer' : '2 cocktails for £12'},
        {'day' : 'Friday', 'start_time' : '16:00', 'end_time' : '19:00', 'offer' : '2 cocktails for £12'}
    ],
    'Foundry Project' : [
        {'day' : 'Sunday', 'start_time' : '15:00', 'end_time' : '21:00', 'offer' : '2 cocktails for £10'},
        {'day' : 'Monday', 'start_time' : '15:00', 'end_time' : '21:00', 'offer' : '2 cocktails for £10'},
        {'day' : 'Tuesday', 'start_time' : '15:00', 'end_time' : '21:00', 'offer' : '2 cocktails for £10'},
        {'day' : 'Wednesday', 'start_time' : '15:00', 'end_time' : '21:00', 'offer' : '2 cocktails for £10'},
        {'day' : 'Thursday', 'start_time' : '15:00', 'end_time' : '21:00', 'offer' : '2 cocktails for £10'}
    ],
    'Pixel Bar' : [
        {'day' : 'Sunday', 'start_time' : '12:00', 'end_time' : '21:00', 'offer' : '2 for 1 cocktails'},
        {'day' : 'Monday', 'start_time' : '16:00', 'end_time' : '21:00', 'offer' : '2 for 1 cocktails'},
        {'day' : 'Tuesday', 'start_time' : '16:00', 'end_time' : '21:00', 'offer' : '2 for 1 cocktails'},
        {'day' : 'Wednesday', 'start_time' : '16:00', 'end_time' : '21:00', 'offer' : '2 for 1 cocktails'},
        {'day' : 'Thursday', 'start_time' : '16:00', 'end_time' : '21:00', 'offer' : '2 for 1 cocktails'},
        {'day' : 'Friday', 'start_time' : '16:00', 'end_time' : '21:00', 'offer' : '2 for 1 cocktails'},
        {'day' : 'Saturday', 'start_time' : '12:00', 'end_time' : '21:00', 'offer' : '2 for 1 cocktails'}
    ],
    '7 Sins' : [
        {'day' : 'Sunday', 'start_time' : '12:00', 'end_time' : '19:00', 'offer' : '2 cocktails for £10'},
        {'day' : 'Monday', 'start_time' : '12:00', 'end_time' : '19:00', 'offer' : '2 cocktails for £10'},
        {'day' : 'Tuesday', 'start_time' : '12:00', 'end_time' : '19:00', 'offer' : '2 cocktails for £10'},
        {'day' : 'Wednesday', 'start_time' : '12:00', 'end_time' : '19:00', 'offer' : '2 cocktails for £10'},
        {'day' : 'Thursday', 'start_time' : '12:00', 'end_time' : '19:00', 'offer' : '2 cocktails for £10'},
        {'day' : 'Friday', 'start_time' : '12:00', 'end_time' : '19:00', 'offer' : '2 cocktails for £10'},
        {'day' : 'Saturday', 'start_time' : '12:00', 'end_time' : '19:00', 'offer' : '2 cocktails for £10'}
    ],
    'Clubhouse' : [
        {'day' : 'Sunday', 'start_time' : '12:00', 'end_time' : '18:00', 'offer' : '2 cocktails for £12'},
        {'day' : 'Monday', 'start_time' : '12:00', 'end_time' : '18:00', 'offer' : '2 cocktails for £12'},
        {'day' : 'Wednesday', 'start_time' : '12:00', 'end_time' : '18:00', 'offer' : '2 cocktails for £12'},
        {'day' : 'Thursday', 'start_time' : '12:00', 'end_time' : '18:00', 'offer' : '2 cocktails for £12'},
        {'day' : 'Friday', 'start_time' : '12:00', 'end_time' : '18:00', 'offer' : '2 cocktails for £12'}
    ],
    'Las Iguanas' : [
        {'day' : 'Sunday', 'start_time' : '11:00', 'end_time' : '23:00', 'offer' : '2 for 1 cocktails'},
        {'day' : 'Monday', 'start_time' : '11:00', 'end_time' : '23:00', 'offer' : '2 for 1 cocktails'},
        {'day' : 'Tuesday', 'start_time' : '11:00', 'end_time' : '23:00', 'offer' : '2 for 1 cocktails'},
        {'day' : 'Wednesday', 'start_time' : '11:00', 'end_time' : '23:00', 'offer' : '2 for 1 cocktails'},
        {'day' : 'Thursday', 'start_time' : '11:00', 'end_time' : '23:00', 'offer' : '2 for 1 cocktails'},
        {'day' : 'Friday', 'start_time' : '11:00', 'end_time' : '23:59', 'offer' : '2 for 1 cocktails'},
        {'day' : 'Saturday', 'start_time' : '11:00', 'end_time' : '23:59', 'offer' : '2 for 1 cocktails'}
    ],
    'Federal': [
        {'day' : 'Sunday', 'start_time' : '09:00', 'end_time' : '23:59', 'offer' : '2 cocktails for £12'},
        {'day' : 'Monday', 'start_time' : '09:00', 'end_time' : '23:59', 'offer' : '2 cocktails for £12'},
        {'day' : 'Tuesday', 'start_time' : '09:00', 'end_time' : '23:59', 'offer' : '2 cocktails for £12'},
        {'day' : 'Wednesday', 'start_time' : '09:00', 'end_time' : '23:59', 'offer' : '2 cocktails for £12'},
        {'day' : 'Thursday', 'start_time' : '09:00', 'end_time' : '23:59', 'offer' : '2 cocktails for £12'},
        {'day' : 'Friday', 'start_time' : '09:00', 'end_time' : '23:59', 'offer' : '2 cocktails for £12'},
        {'day' : 'Saturday', 'start_time' : '09:00', 'end_time' : '23:59', 'offer' : '2 cocktails for £12'}
    ],
    'Lonocove (NQ)' : [
        {'day' : 'Monday', 'start_time' : '16:00', 'end_time' : '23:59', 'offer' : '£6 cocktails'},
        {'day' : 'Tuesday', 'start_time' : '16:00', 'end_time' : '23:59', 'offer' : '£6 cocktails'},
        {'day' : 'Wednesday', 'start_time' : '16:00', 'end_time' : '23:59', 'offer' : '£6 cocktails'},
        {'day' : 'Thursday', 'start_time' : '16:00', 'end_time' : '23:59', 'offer' : '£6 cocktails'},
        {'day' : 'Friday', 'start_time' : '16:00', 'end_time' : '20:00', 'offer' : '£6 cocktails'},
        {'day' : 'Saturday', 'start_time' : '13:00', 'end_time' : '20:00', 'offer' : '£6 cocktails'},
    ],
    'Be At One' : [
        {'day' : 'Sunday', 'start_time' : '15:00', 'end_time' : '19:00', 'offer' : '2 for 1 cocktails'},
        {'day' : 'Monday', 'start_time' : '16:00', 'end_time' : '19:00', 'offer' : '2 for 1 cocktails'},
        {'day' : 'Tuesday', 'start_time' : '16:00', 'end_time' : '19:00', 'offer' : '2 for 1 cocktails'},
        {'day' : 'Wednesday', 'start_time' : '16:00', 'end_time' : '19:00', 'offer' : '2 for 1 cocktails'},
        {'day' : 'Thursday', 'start_time' : '16:00', 'end_time' : '19:00', 'offer' : '2 for 1 cocktails'},
        {'day' : 'Friday', 'start_time' : '15:00', 'end_time' : '19:00', 'offer' : '2 for 1 cocktails'},
        {'day' : 'Saturday', 'start_time' : '12:00', 'end_time' : '18:00', 'offer' : '2 for 1 cocktails'}
    ],
    'Onn Bar (Gay Vilage)' : [
        {'day' : 'Tuesday', 'start_time' : '09:00', 'end_time' : '23:59', 'offer' : '2 for 1 cocktails'}
    ],
    'The Blues Kitchen' : [
        {'day' : 'Wednesday', 'start_time' : '09:00', 'end_time' : '23:59', 'offer' : '£6 cocktails'}
    ],
    'Motley (Deansgate)' : [
        {'day' : 'Monday', 'start_time' : '17:00', 'end_time' : '20:00', 'offer' : '2 for 1 cocktails'},
        {'day' : 'Tuesday', 'start_time' : '17:00', 'end_time' : '20:00', 'offer' : '2 for 1 cocktails'},
        {'day' : 'Wednesday', 'start_time' : '17:00', 'end_time' : '20:00', 'offer' : '2 for 1 cocktails'},
        {'day' : 'Thusday', 'start_time' : '17:00', 'end_time' : '20:00', 'offer' : '2 for 1 cocktails'},
        {'day' : 'Friday', 'start_time' : '17:00', 'end_time' : '20:00', 'offer' : '2 for 1 cocktails'}
    ],
    'Slug & Lettuce' : [
        {'day' : 'Sunday', 'start_time' : '12:00', 'end_time' : '23:00', 'offer' : '2 for 1 cocktails'},
        {'day' : 'Monday', 'start_time' : '16:00', 'end_time' : '23:00', 'offer' : '2 for 1 cocktails'},
        {'day' : 'Tuesday', 'start_time' : '16:00', 'end_time' : '23:00', 'offer' : '2 for 1 cocktails'},
        {'day' : 'Wednesday', 'start_time' : '16:00', 'end_time' : '23:00', 'offer' : '2 for 1 cocktails'},
        {'day' : 'Thursday', 'start_time' : '16:00', 'end_time' : '23:00', 'offer' : '2 for 1 cocktails'},
        {'day' : 'Friday', 'start_time' : '12:00', 'end_time' : '23:00', 'offer' : '2 for 1 cocktails'},
        {'day' : 'Saturday', 'start_time' : '12:00', 'end_time' : '23:00', 'offer' : '2 for 1 cocktails'}
    ],
    'Revolution' : [
        {'day' : 'Sunday', 'start_time' : '09:00', 'end_time' : '23:59', 'offer' : '2 cocktails for £10'},
        {'day' : 'Monday', 'start_time' : '09:00', 'end_time' : '23:59', 'offer' : '2 cocktails for £10'},
        {'day' : 'Tuesday', 'start_time' : '09:00', 'end_time' : '23:59', 'offer' : '2 cocktails for £10'},
        {'day' : 'Wednesday', 'start_time' : '09:00', 'end_time' : '23:59', 'offer' : '2 cocktails for £10'},
        {'day' : 'Thursday', 'start_time' : '09:00', 'end_time' : '23:59', 'offer' : '2 cocktails for £10'},
        {'day' : 'Friday', 'start_time' : '09:00', 'end_time' : '23:59', 'offer' : '2 cocktails for £10'}
    ],
    'The Oxnoble (Liverpool Road)' : [
        {'day' : 'Sunday', 'start_time' : '09:00', 'end_time' : '23:59', 'offer' : '2 for 1 cocktails'},
        {'day' : 'Monday', 'start_time' : '09:00', 'end_time' : '23:59', 'offer' : '2 for 1 cocktails'},
        {'day' : 'Tuesday', 'start_time' : '09:00', 'end_time' : '23:59', 'offer' : '2 for 1 cocktails'},
        {'day' : 'Wednesday', 'start_time' : '09:00', 'end_time' : '23:59', 'offer' : '2 for 1 cocktails'},
        {'day' : 'Thursday', 'start_time' : '09:00', 'end_time' : '23:59', 'offer' : '2 for 1 cocktails'},
        {'day' : 'Friday', 'start_time' : '09:00', 'end_time' : '23:59', 'offer' : '2 for 1 cocktails'},
        {'day' : 'Saturday', 'start_time' : '09:00', 'end_time' : '23:59', 'offer' : '2 for 1 cocktails'}
    ],
    'Manhatta' : [
        {'day' : 'Sunday', 'start_time' : '09:00', 'end_time' : '23:59', 'offer' : '2 for 1 cocktails'},
        {'day' : 'Monday', 'start_time' : '09:00', 'end_time' : '23:59', 'offer' : '2 for 1 cocktails'},
        {'day' : 'Tuesday', 'start_time' : '09:00', 'end_time' : '23:59', 'offer' : '2 for 1 cocktails'},
        {'day' : 'Wednesday', 'start_time' : '09:00', 'end_time' : '23:59', 'offer' : '2 for 1 cocktails'},
        {'day' : 'Thursday', 'start_time' : '09:00', 'end_time' : '23:59', 'offer' : '2 for 1 cocktails'},
        {'day' : 'Friday', 'start_time' : '09:00', 'end_time' : '23:59', 'offer' : '2 for 1 cocktails'}
    ],
    'Banyan Tree (Castlefield)' : [
        {'day' : 'Monday', 'start_time' : '17:30', 'end_time' : '19:30', 'offer' : '2 cocktails for £12'},
        {'day' : 'Tuesday', 'start_time' : '19:00', 'end_time' : '21:00', 'offer' : '2 cocktails for £12'},
        {'day' : 'Wednesday', 'start_time' : '19:00', 'end_time' : '21:00', 'offer' : '2 cocktails for £12'},
        {'day' : 'Thursday', 'start_time' : '19:00', 'end_time' : '21:00', 'offer' : '2 cocktails for £12'},
        {'day' : 'Friday', 'start_time' : '19:00', 'end_time' : '21:00', 'offer' : '2 cocktails for £12'},
        {'day' : 'Saturday', 'start_time' : '19:00', 'end_time' : '21:00', 'offer' : '2 cocktails for £12'},
        {'day' : 'Sunday', 'start_time' : '16:00', 'end_time' : '20:00', 'offer' : '2 cocktails for £12'}
    ],
    'Barca (Castlefield)' : [
        {'day' : 'Sunday', 'start_time' : '11:00', 'end_time' : '23:00', 'offer' : '2 for 1 cocktails'},
        {'day' : 'Monday', 'start_time' : '11:00', 'end_time' : '23:00', 'offer' : '2 for 1 cocktails'},
        {'day' : 'Tuesday', 'start_time' : '11:00', 'end_time' : '23:00', 'offer' : '2 for 1 cocktails'},
        {'day' : 'Wednesday', 'start_time' : '11:00', 'end_time' : '23:00', 'offer' : '2 for 1 cocktails'},
        {'day' : 'Thursday', 'start_time' : '11:00', 'end_time' : '23:00', 'offer' : '2 for 1 cocktails'},
        {'day' : 'Friday', 'start_time' : '11:00', 'end_time' : '23:59', 'offer' : '2 for 1 cocktails'},
        {'day' : 'Saturday', 'start_time' : '11:00', 'end_time' : '23:59', 'offer' : '2 for 1 cocktails'}
    ],
    'Turtle Bay' : [
        {'day' : 'Sunday', 'start_time' : '11:00', 'end_time' : '19:00', 'offer' : '2 for 1 cocktails'},
        {'day' : 'Sunday', 'start_time' : '21:30', 'end_time' : '23:59', 'offer' : '2 for 1 cocktails'},
        {'day' : 'Monday', 'start_time' : '11:00', 'end_time' : '19:00', 'offer' : '2 for 1 cocktails'},
        {'day' : 'Monday', 'start_time' : '21:30', 'end_time' : '23:30', 'offer' : '2 for 1 cocktails'},
        {'day' : 'Tuesday', 'start_time' : '11:00', 'end_time' : '19:00', 'offer' : '2 for 1 cocktails'},
        {'day' : 'Tuesday', 'start_time' : '21:30', 'end_time' : '23:30', 'offer' : '2 for 1 cocktails'},
        {'day' : 'Wednesday', 'start_time' : '11:00', 'end_time' : '19:00', 'offer' : '2 for 1 cocktails'},
        {'day' : 'Wednesday', 'start_time' : '21:30', 'end_time' : '23:30', 'offer' : '2 for 1 cocktails'},
        {'day' : 'Thursday', 'start_time' : '11:00', 'end_time' : '19:00', 'offer' : '2 for 1 cocktails'},
        {'day' : 'Thursday', 'start_time' : '21:30', 'end_time' : '23:59', 'offer' : '2 for 1 cocktails'},
        {'day' : 'Friday', 'start_time' : '11:00', 'end_time' : '19:00', 'offer' : '2 for 1 cocktails'},
        {'day' : 'Friday', 'start_time' : '21:30', 'end_time' : '23:59', 'offer' : '2 for 1 cocktails'},
        {'day' : 'Saturday', 'start_time' : '10:00', 'end_time' : '19:00', 'offer' : '2 for 1 cocktails'},
        {'day' : 'Saturday', 'start_time' : '21:30', 'end_time' : '23:59', 'offer' : '2 for 1 cocktails'},
    ]
}

# strptime is string parse time
# %H:%M is 24h time from datetime
# %A is day of the week from datetime
# strftime is string function time

for venue, offers in happy_hour_offers.items():
    for promotion in offers:
        start = datetime.datetime.strptime(promotion['start_time'], '%H:%M').time()
        end = datetime.datetime.strptime(promotion['end_time'], '%H:%M').time()
        if promotion['day'].lower() == now.strftime('%A').lower() and start <= now.time() <= end:
            print(f"At {venue}, {promotion['offer']} is available now")


# Another thing to include:
# How to amend it for bars that are open past 23:59? E.g. Barca is open until 03:00 Fri & Sat night (Sat & Sun morning)
# Adding "until...[end_time]" to the output.