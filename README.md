# Vin Decoder
## This program takes the vehicle's VIN code and decodes it, showing information such as: region of manufacture, country of the vehicle, year of manufacture, vehicle make.
![ссылка_на_изображение](https://dmv-permit-test.com/images/vin-decoder.png)

### Swagger http://localhost:8000/api/swagger/
<br>

# Installation:
<br>

## Clone repository:
```git clone https://github.com/IvanAshikhin/VIN_decoder_proj.git```
<br>

## Install Dependencies using Poetry:
```poetry install```
<br>

## Activate the Virtual Environment:
```poetry shell```
<br>

## Build and Run Docker Container:
```docker-compose up --build```
<br>

## Apply Migrations within Docker Container:
```docker-compose exec web python manage.py migrate```
<br>

## Run the Development Server:
```docker-compose up```
<br>
<br>

# Contributors
https://github.com/IvanAshikhin
