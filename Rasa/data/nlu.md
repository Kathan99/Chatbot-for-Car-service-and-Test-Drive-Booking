## intent:greet
- hey
- hello
- hi
- good morning
- good evening
- hey there

## intent:goodbye
- bye
- goodbye
- see you around
- see you later

## intent:serviceneed
- I want service booking help
- I need help with service 
- Service Booking
- Really need help with Service booking

## intent:testdriveneed
- I want test drive booking today
- I need help with test drive
- Test Drive Booking
- Really need help with Test drive booking


## intent:carselect
- I want details of [Figo](testcar)
- I want details of [Endeavour](testcar)
- I want details of [Ecosport](testcar)
- Information of [Freestyle](testcar)
- Information of [Aspire](testcar)
- Show me some information of [Mustang](testcar)
- I want details of [Edge](testcar)
- Information of [Explorer](testcar)
- Inormation of [Focus](testcar) 


## intent:choosecar
- I want to select [Figo](testdrivecar)
- I want to select [Endeavour](testdrivecar)
- Book me [Ecosport](testdrivecar)
- Book me [Freestyle](testdrivecar)
- Book me [Aspire](testdrivecar)
- I want test drive booking of [Mustang](testdrivecar)
- I want test drive booking of [Edge](testdrivecar)
- My preferred car is [Explorer](testdrivecar)
- My preferred car is [Focus](testdrivecar) 

## intent:inform
- My customerid is [1](cid)
- Customerid is [2](cid)
- My customerid is [3](cid)
- CID is [8](cid)
- Customerid is [14](cid)
- CID is [12](cid)

## intent:customername
- My name is [Aashish](cname)
- My name is [Aakash](cname)
- My name is [Aabhas](cname)
- My name is [Aadarsh](cname)
- My name is [Abhay](cname)
- My name is [Abhijit](cname)
- My name is [Adil](cname)
- My name is [Ananaya](cname)
- My name is [Bhargav](cname)
- My name is [Badrinath](cname)
- My name is [Bagira](cname)
- My name is [Bina](cname)
- My name is [Bimal](cname)
- My name is [Binita](cname)
- My name is [Bansari](cname)
- My name is [Bali](cname)
- My name is [Chandrika](cname)
- My name is [Chetna](cname)
- My name is [Chameli](cname)
- My name is [Chandsi](cname)
- My name is [Chandni](cname)
- My name is [Chatur](cname)
- My name is [Chandu](cname)
- My name is [Chaman](cname)
- My name is [Damodar](cname)
- My name is [Dimpal](cname)
- My name is [Diana](cname)
- My name is [Dolli](cname)

## lookup:cname
   data/name.txt

## intent:vehiclename
- Name of the car is [AStar](carname)
- Name of the car is [Alto](carname)
- Name of the car is [Baleno](carname)
- Name of the car is [Calerio](carname)
- Name of the car is [Ciaz](carname)
- Name of the car is [Dzire](carname)
- Name of the car is [Eeco](carname)
- Name of the car is [Ertiga](carname)
- Name of the car is [Esteem](carname)
- Name of the car is [Grand Vitara](carname)
- Name of the car is [Gypsy](carname)
- Name of the car is [Ignis](carname)
- Name of the car is [Omni](carname)
- Name of the car is [Ritz](carname)
- Name of the car is [Swift](carname)
- Name of the car is [Wagonr](carname)
- [AStar](carname)
- [Alto](carname)
- [Baleno](carname)
- [Celerio](carname)
- [Ciaz](carname)
- [Dzire](carname)
- [Eeco](carname)
- [Ertiga](carname)
- [Esteem](carname)
- [Grand Vitara](carname)
- [Gypsy](carname)
- [Ignis](carname)
- [Omni](carname)
- [Ritz](carname)
- [Swift](carname)
- [Wagonr](carname)

## lookup:carname
   data/brand.txt

## intent:fuel
- [Petrol](fueltype)
- [Diesel](fueltype)

## intent:testcarsedan
- [Sedan](testsedan)
- I want to book [Sedan](testsedan)
- [Sedan](testsedan) is best option for me
- I want [Sedan](testsedan)
- Can you show me [Sedan](testsedan)

## intent:testcarsuv
- [SUV](testsuv)
- I want to book [SUV](testsuv)
- [SUV](testsuv) is best option for me
- I want [SUV](testsuv)
- Can you show me [SUV](testsuv)

## intent:testcarhatchback
- [Hatchback](testhatchback)
- I want to book [Hatchback](testhatchback)
- [Hatchback](testhatchback) is best option for me
- I want [Hatchback](testhatchback)
- Can you show me [Hatchback](testhatchback)

## intent:testcarcrossover
- [Crossover](testcrossover)
- I want to book [Crossover](testcrossover)
- [Crossover](testcrossover) is best option for me
- I want [Crossover](testcrossover)
- Can you show me [Crossover](testcrossover)

## intent:cphone
- Contact number is [1234567890](phone)
- Contact number is [9408029036](phone)
- Phone Number is [4735234938](phone)
- [6354238945](phone)
- [6983493384](phone)
- [7890453856](phone)
- [7184934687](phone)
- [9374874924](phone)
- [9404934742](phone)
- [8792832973](phone)
- [9248728747](phone)
- [9934862364](phone)
- [8538757356](phone)
- [6628497244](phone)

## regex:phone
 - [0-9]{10}

## intent:affirm
- indeed
- yes
- yo
- Ok
- I am ready
- Woohoo
- Ready
- Great
- Yes I am ready

## intent:confirmation
- Ok I want to book the car
- I want to continue with the booking
- I need to book the test drive
- I want to register for the test drive
- I am glad to book the service
- Register me for test drive
- Book a Test Drive 
- Please I want to go ahead
- I want to go ahead

## intent:confirm
- I want to continue
- I want to fill the form again
- I was out of my mind
- Can you start slot filling again
- I am interested
- I want to start 
- I am ready for the booking

## intent:deny
- no
- never
- I don't think so
- don't like that
- no way
- not really
- I don't have customerid
- I don't need any help
- I have changed my mind
- I don't want to go ahead

## intent:out_of_scope
- Stop
- Get out
- Pizza
- I am going to die
- Why sky is blue
- Why orange is orange
- Why grass is green
- I may see a movie today 
- What you doing
- Privacy issue
- Oh god
- How hurtful is this
- Why god I am doing this

## intent:bot_challenge
- are you a bot?
- are you a human?
- am I talking to a bot?
- am I talking to a human?
