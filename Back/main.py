'''
  Developed by Brayan Cataño Giraldo.
  E-mail: b.catano@utp.edu.co
'''

'''
	This file contains the main file.
	It is used to run the application.
'''
# Importing libraries
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from config.database import engine, Base

# Importing middlewares
from middlewares.error_handler import ErrorHandler
from fastapi.middleware.cors import CORSMiddleware

# Importing models
from models.flowershops import FlowerShop
from models.providers import Provider
from models.products import Product
from models.inventory import Inventory
from models.users import User

# Importing routers
from routes.flowershop import flowerShop_router
from routes.user import user_router
from routes.providers import providers_router
from routes.products import products_router

app = FastAPI()

app.title = "My flower shop inventory application."
app.version = "0.3.0"

# Middlewares
app.add_middleware(ErrorHandler)
app.add_middleware(
    CORSMiddleware, 
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(flowerShop_router)
app.include_router(user_router)
app.include_router(providers_router)
app.include_router(products_router)

# Creating tables
Base.metadata.create_all(bind=engine)

# Welcome message
@app.get("/", tags=["Main"])
def message():
	return JSONResponse(content={ 
		"Welcome_message": "Welcome to the DataFlor backend!",
		"flowerShops (LISTO)": {
			"allFlowerShops": "GET /flower-shops",
			"flowerShopById": "GET /flower-shops/:id",
			"flowerShopByName": "GET /flower-shops/name/:name",
			"flowerShopByAddress": "GET /flower-shops/address/:address",
			"flowerShopByPhone": "GET /flower-shops/phone/:phone",
			"flowerShopByState": "GET /flower-shops/state/:state",
			"createFlowerShop": "POST /flower-shops/create",
			"updateFlowerShopById": "PUT /flower-shops/update/id/:id",
			"updateFlowerShopByFullname": "PUT /flower-shops/update/fullname/:name"
		},
		"users (LISTO)": {
			"allUsers": "GET /users",
			"userById": "GET /users/:id",
			"userByUsername": "GET /users/username/:name",
			"userByFullName": "GET /users/fullName/:fullName",
			"userByPhone": "GET /users/phone/:phone",
			"userByRole": "GET /users/role/:role",
			"userByIdflowerShops": "GET /users/idflowerShops/:idflowerShops",
			"userByState": "GET /users/state/:state",
			"createUser": "POST /users/create",
			"login": "POST /login",
			"updateUserById": "PUT /users/update/id/:id",
			"updateUserByUsername": "PUT /users/update/username/:name"
		},
		"providers (LISTO)": {
			"allProviders": "GET /providers",
			"providerById": "GET /providers/:id",
			"providerByName": "GET /providers/name/:name",
			"providerByPhone": "GET /providers/phone/:phone",
			"providerByAddress": "GET /providers/address/:address",
			"providerByState": "GET /providers/state/:state",
			"createProvider": "POST /providers/create",
			"updateProviderById": "PUT /providers/update/id/:id",
			"updateProviderByFullname": "PUT /providers/update/fullname/:name"
		},
		"products (LISTO)": {
			"allProducts": "GET /products",
			"productById": "GET /products/:id",
			"productByName": "GET /products/name/:name",
			"createProduct": "POST /products/create",
			"updateProduct": "PUT /products/update/id/:id"
		},
		"inventory": {
			"allInventory": "GET /inventory",
			"inventoryById": "GET /inventory/:id",
			"inventoryByIdflowerShops": "GET /inventory/idflowershops/:idflowerShops",
			"createInventory": "POST /inventory/create",
			"updateInventory": "PUT /inventory/update/id/:id"
		}
	}
)
