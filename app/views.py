from flask import render_template
from app import app
from datetime import date,time,timedelta

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Miguel'}  # fake user
    events = [
        {
            'date':date(2017,07,06),
            'name':'Thursday Night Summer Series',
            'races':[
                {
                    'raceNum':1,
                    'startTime':time(18,30,00),
                    'course':{
                        'name':1,
                        'description':'Windward-leeward, marks to port',
                        'length':1738.092,
                        'location':{
                            'name':'Stony Creek Metropark',
                            'latitude':42.718481,
                            'longitude':-83.084106
                        },
                        'marks':[
                            {
                                'name':'W-START',
                                'index':0,
                                'latitude':42.719,
                                'longitude':-83.0883333,
                                'starboardRounding':False,
                                'start':True,
                                'finish':False
                            },
                            {
                                'name':'E-START',
                                'index':0,
                                'latitude':42.719,
                                'longitude':-83.0875,
                                'starboardRounding':False,
                                'start':True,
                                'finish':False
                            },
                            {
                                'name':'1B',
                                'index':1,
                                'latitude':42.725,
                                'longitude':-83.0879167,
                                'starboardRounding':False,
                                'start':False,
                                'finish':False
                            },
                            {
                                'name':'3',
                                'index':2,
                                'latitude':42.7171667,
                                'longitude':-83.0879167,
                                'starboardRounding':False,
                                'start':False,
                                'finish':False
                            },
                            {
                                'name':'W-START',
                                'index':3,
                                'latitude':42.719,
                                'longitude':-83.0883333,
                                'starboardRounding':False,
                                'start':False,
                                'finish':True
                            },
                            {
                                'name':'E-START',
                                'index':3,
                                'latitude':42.719,
                                'longitude':-83.0875,
                                'starboardRounding':False,
                                'start':False,
                                'finish':True
                            },
                        ]
                    },
                    'cfResults':[
                        {
                            'place':1,
                            'skipper':'Andrew Meyer',
                            'boat':{
                                'sailNum':340,
                                'make':'MFG',
                                'model':'Pintail',
                                'length':14,
                                'units':'feet',
                                'portsmouthHC':105
                            },
                            'time':timedelta(minutes=21,seconds=38.99),
                            'handicap':0.98,
                            'nextHandicap':0.98,
                            'corrected':timedelta(seconds=(timedelta(minutes=21,seconds=38.99).total_seconds()*.98)),
                            'shortCourse':False
                        },
                        {
                            'place':2,
                            'skipper':'Marc Meyer',
                            'boat':{
                                'sailNum':340,
                                'make':'MFG',
                                'model':'Pintail',
                                'length':14,
                                'units':'feet',
                                'portsmouthHC':105
                            },
                            'time':timedelta(minutes=21,seconds=37.99),
                            'handicap':1.01,
                            'nextHandicap':1.01,
                            'corrected':timedelta(seconds=(timedelta(minutes=21,seconds=37.99).total_seconds()*1.01)),
                            'shortCourse':False
                        },
                    ]

    ]

    return render_template('index.html',
#                           title='Home',
                            user=user,
                            events=events)
