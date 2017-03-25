## MeteoKL integration
Integration with [weather station](http://www.computerlink.ru/node/39) that consists of two components:

 1. **worker.py** that collects data from weather station and writes it to the sqlite database *weather.db* periodically
 2. **server.py** that makes server to show latest weather data in pretty self-updating html page

### Installation
**Note:** Python 3 is required  
```
pip install -r requirements.txt
python setup.py
```
Last command just creates database's tables  
Now open **config.py** and edit configuration (all details are described in file)  

### Running
Plugin your [weather station](http://www.computerlink.ru/node/39) to your computer and run the following commands:
```
python server.py
```
To start server on **localhost** at port you have specified in **config.py**  
```
python worker.py
```
To start collecting data from weather station  
**Note:** If page is not displaying numbers just wait for some time - this means that worker haven't recorded any data to database yet
