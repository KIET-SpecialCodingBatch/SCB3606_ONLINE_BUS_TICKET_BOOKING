from flask import Flask, render_template, request 
from datetime import datetime,timedelta


app = Flask(__name__)

area={ '1':'Hyderabad','2':'Tirupati','3':'Chennai','4': 'Banglore','5':'Vijayawada','6':'Vishakapatnam'}

prices={
    '1': {
        '2': 500,
        '3': 654,
        '4': 865,
        '5' :395,
        '6' :570 },
    '2': {
        '1': 515,
        '3': 150 ,
        '4': 330,
        '5' :390,
        '6' : 785
    },
    '3': {
        '2': 150,
        '1': 654,
        '4': 445,
        '5' :545,
        '6' :1150
    },
    '4': {
        '2': 330,
        '1': 865,
        '3': 445,
        '5' :545,
        '6' :1150
    },
    '5': {
        '2': 390,
        '1': 395,
        '4': 545,
        '3' :545,
        '6' :605
    },
    '6': {
        '2': 785,
        '1': 570,
        '4': 1150,
        '5' :605,
        '3' :1230
    }
}

time={('1','2'):10,('1','3'):12,('1','4'):10,('1','5'):5,('1','6'):12,('2','1'):10,('2','3'):4,('2','4'):5,('2','5'):9,('2','6'):15,
      ('3','1'):12,('3','2'):4,('3','4'):8,('3','5'):9,('3','6'):15,
      ('4','1'):10,('4','2'):5,('4','3'):7,('4','5'):13,('4','6'):19,('5','1'):5,('5','2'):8,('5','3'):9,('5','4'):13,('5','6'):7,
      ('6','1'):12,('6','2'):12,('6','3'):15,('6','4'):19,('6','5'):7 }

@app.route('/',methods=['GET','POST'])
def index():
    return render_template('index.html')

@app.route('/greet', methods=['GET','POST'])


def greet():
    
    if request.method=="POST":

        Name = request.form.get("Name")
        dep_name = request.form.get("From")
        dep=area.get(dep_name)
        
        area_name=request.form.get("To")
        areas=area.get(area_name)
        Tickets = int(request.form.get("Tickets"))
       
        Time = request.form.get("Time")
        price = prices.get(dep_name,{}).get(area_name)
        date = request.form.get("Date")
        Mobile = request.form.get("Mobile")
        if price is not None:
            difprices = Tickets * price
        else:
            difprices = 0
        dtime = calculate_time(dep_name, area_name, Time)
       


        return render_template('greet.html', Name=Name, From=dep, To=areas, Tickets=Tickets, Time=Time, Date=date, Mobile=Mobile,difprices=difprices,dtime=dtime)
    
    return render_template('greet.html', From='', To='', Time='', departure_time='')

def calculate_time(dep_name,area_name,Time):
    travel_hours = time.get((dep_name, area_name))

    if travel_hours is None:
        return None

    try:
        arriving_time_obj = datetime.strptime(Time, "%H:%M")
        departure_time_obj = arriving_time_obj - timedelta(hours=int(travel_hours))
        departure_time = departure_time_obj.strftime("%H:%M")
        return departure_time
    except ValueError:
        return None
        
    
    
   
if __name__ == '__main__':
    app.run(debug=True)

 
    


