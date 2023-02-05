function pizzaOven(crustType, sauceType, cheese, toppings){
    var pizza = {};
    pizza.crustType= crustType;
    pizza.sauceType=sauceType;
    pizza.cheese=cheese;
    pizza.toppings=toppings;
    return pizza;
}

var pizza1 = pizzaOven("deep dish", "traditional", ["mozzarella"], ["pepperoni", "sausage"])
var pizza2 = pizzaOven("hand tossed", "marinara", ["mozzarella", "feta"], ["mushrooms", "olives", "onions"])
var pizza3 = pizzaOven("deep dish", "white", ["mozzarella"], ["truffle"])
var pizza4 = pizzaOven("neopolitan", "marinara", ["mozzarella"], ["mushrooms", "truffle", "egg"])

console.log(pizza3);