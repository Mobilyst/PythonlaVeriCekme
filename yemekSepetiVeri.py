
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from fake_useragent import UserAgent
import time
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use the application default credentials.
cred = credentials.Certificate("mobilyst-135d1-firebase-adminsdk-ok765-4049e4f57f.json")

firebase_admin.initialize_app(cred)
db = firestore.client()

# Create Chromeoptions instance 
options = webdriver.ChromeOptions() 

# Adding argument to disable the AutomationControlled flag 
options.add_argument("--disable-blink-features=AutomationControlled") 
 
# Exclude the collection of enable-automation switches 
options.add_experimental_option("excludeSwitches", ["enable-automation"]) 
 
# Turn-off userAutomationExtension 
options.add_experimental_option("useAutomationExtension", False) 

def get_random_user_agent():
	ua = UserAgent()
	userAgent = ua.opera
	if "Macintosh" in userAgent or "MSIE 6.0" in userAgent:
		return get_random_user_agent()
	return userAgent

userAgent = get_random_user_agent()
print(userAgent)
options.add_argument(f'user-agent={userAgent}')

# Setting the driver path and requesting a page 
driver = webdriver.Chrome(options=options) 
 
# Changing the property of the navigator value for webdriver to undefined 
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

def getByCity(city):
	driver.get("https://www.yemeksepeti.com/city/" + city)
	time.sleep(5)
	# driver.find_element("id", "email").send_keys(username)
	time.sleep(50000)
	# driver.find_element_by_xpath('//button[normalize-space()="Devam Et"]')
	time.sleep(5)

def getRestaurantsByLocation(lat, lng):
	driver.get(f"https://www.yemeksepeti.com/restaurants/new?lat={lat}&lng={lng}&vertical=restaurants")
	time.sleep(10)
	restaurants = [];
	restaurant_urls = driver.find_elements(By.CSS_SELECTOR, "section.vendor-list-section.open-section a")
	restaurant_names = driver.find_elements(By.CSS_SELECTOR, "section.vendor-list-section.open-section span.name.fn")
	for i in range(len(restaurant_urls)):
		restaurants.append({"name": restaurant_names[i].get_attribute('innerText'), "url": restaurant_urls[i].get_attribute("href")})
	return restaurants
	print(x)
	
	time.sleep(5000)
 
def getRestaurants(restaurant):
	driver.get(restaurant)
	time.sleep(10)
	restaurants = [];
	restaurant_urls = driver.find_elements(By.CSS_SELECTOR, "section.vendor-list-section.open-section a")
	restaurant_names = driver.find_elements(By.CSS_SELECTOR, "section.vendor-list-section.open-section span.name.fn")
	for i in range(len(restaurant_urls)):
		restaurants.append({"name": restaurant_names[i].get_attribute('innerText'), "url": restaurant_urls[i].get_attribute("href")})
	return restaurants
	print(x)
	
	time.sleep(5000)

def getMenu(restaurant):
	print(restaurant['url'])
	userAgent = get_random_user_agent()
	options.add_argument(f'user-agent={userAgent}')
	driver.get(restaurant['url'])
	time.sleep(10)
	products = []
	product_elements = driver.find_elements(By.CSS_SELECTOR, 'li[data-testid="menu-product"]')
	print(product_elements)
	for i in range(len(product_elements)):
		ActionChains(driver).move_to_element(product_elements[i]).perform()
		try:
			name = product_elements[i].find_element(By.CSS_SELECTOR, '[data-testid="menu-product-name"]').get_attribute("innerText")
		except:
			name = "null"

		try:
			image_url = product_elements[i].find_element(By.CSS_SELECTOR, 'div[data-testid="menu-product-image"]').get_attribute("style").replace('background-image: url("', '').replace('");', '')
		except:
			image_url = "null"
		
		try:
			price = product_elements[i].find_element(By.CSS_SELECTOR, '[data-testid="menu-product-price"]').get_attribute("innerText")
		except:
			price = "null"
		
		product_url = restaurant['url']
		products.append({
			"name": name,
			"image_url": image_url,
			"price": price,
			"product_url": product_url 
		})
		for product in products:
			db.collection("products").document(f"{name}").set(product)	


#malatya = 38.3520108, 38.3364161
#ankara = 39.93023370999475, 32.86232043724655
restaurants = getRestaurantsByLocation(38.3520108, 38.3364161)
print(restaurants)
index=2
for restaurant in restaurants:

	userAgent = get_random_user_agent()
	options.add_argument(f'user-agent={userAgent}')
	getMenu(restaurants[index])
	