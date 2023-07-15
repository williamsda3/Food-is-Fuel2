# Importing the request module
import requests

API_KEY = '33edc764ecf341ef9b75704f6297816e'

# Creating a function to return recipe suggestions based on ingredients passed
def get_recipe_suggestions(ingredients):
    endpoint = 'https://api.spoonacular.com/recipes/complexSearch'
    params = {
        'apiKey': API_KEY,
        'includeIngredients': ','.join(ingredients),
        'cuisine': cuisine,
        'type': mealType,
        'diet' : diet,
        'intolerances': intolerances, 
        'number': number  # Number of recipe suggestions to retrieve
    }

    response = requests.get(endpoint, params=params)
    if response.status_code == 200:
        recipe_suggestions = response.json()
        for recipe in recipe_suggestions['results']:
            recipe_title = recipe['title']
            recipe_id = recipe['id']
            print(f"Recipe: {recipe_title} (ID: {recipe_id})")
    else:
        print('Failed to retrieve recipe suggestions.')


# Creating an array to hold the ingredients
ingredients = []
# Creating arrays to hold the different filter preferences
cuisine = []
mealType = []
diet = []
intolerances = []

# Prompt the user to select number of desired recipes
number = input('Number of recipe suggestions \n>> ')

# Creating boolean variables to control menu flow
finished = False
filterFinished = False
exitProgram = False

# Display a 'menu' that loops and adds search filters based on the users input
while not filterFinished:
    filters = input('\n What filters would you like to add? (Enter 0 to skip)\n 0) Skip \n 1) Cuisine \n 2) Meal Type \n 3) Diet \n 4) Intolerances \n 00) Close Program \n>> ')
    match filters:
        
        case "00":   
            finished = True
            break
        
        case "0":   
            filterFinished = True
        case "1":
            cuisine.append(input("-----Enter cuisine preference \n>> "))

        case "2":
            mealType.append(input("-----Enter meal type preference \n>> "))

        case "3":
            diet.append(input("-----Enter diet preference \n>> "))
            
        case "4":
            intolerances.append(input("-----Enter intolerances \n>> "))
            
# Get an store ingredients
while not finished:
    recipe1 = input('Enter a desired ingredient: (Enter 0 to exit)\n>> ')
    if recipe1 == '0':
        finished = True
    else: 
        ingredients.append(recipe1)
        
# Display recipes that fit users search criteria
get_recipe_suggestions(ingredients)
