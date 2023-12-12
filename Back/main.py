from fastapi import FastAPI
from fastapi.responses import JSONResponse
from config.database import engine, Base

from middlewares.error_handler import ErrorHandler

# Importing models
from models.flowershops import FlowerShop
from models.providers import Provider
from models.products import Product
from models.inventory import Inventory
from models.users import User

# Importing routers
from routers.flowershop import flowerShop_router

app = FastAPI()

app.title = "My flower shop inventory application."
app.version = "0.1.0"

# Middlewares
app.add_middleware(ErrorHandler)

# Routers
app.include_router(flowerShop_router)

# Creating tables
Base.metadata.create_all(bind=engine)

# Welcome message
@app.get("/", tags=["Main"])
def message():
	return JSONResponse(content={ 
		"Welcome_message": "Welcome to the DataFlor backend!",
		"flowerShops": {
			"allFlowerShops": "GET /flower-shops (LISTO)",
			"flowerShopById": "GET /flower-shops/:id (LISTO)",
			"flowerShopByName": "GET /flower-shops/name/:name (LISTO)",
			"flowerShopByAddress": "GET /flower-shops/address/:address (LISTO)",
			"flowerShopByPhone": "GET /flower-shops/phone/:phone (LISTO)",
			"flowerShopByState": "GET /flower-shops/state/:state (LISTO)",
			"createFlowerShop": "POST /flower-shops/create (LISTO)",
			"updateFlowerShopById": "PUT /flower-shops/update/id/:id",
			"updateFlowerShopByFullname": "PUT /flower-shops/update/fullname/:name"
		},
		"users": {
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
		"providers": {
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
		"products": {
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

