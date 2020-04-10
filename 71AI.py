from random import randint


def diet():
    protein = ['Yogurt(1 cup)','Cooked meat(3 Oz)','Cooked fish(4 Oz)','1 whole egg + 4 egg whites','Tofu(5 Oz)']
    fruit = ['Berries(80 Oz)','Apple','Orange','Banana','Dried Fruits(Handfull)','Fruit Juice(125ml)']
    vegetable = ['Any vegetable(80g)']
    grains = ['Cooked Grain(150g)','Whole Grain Bread(1 slice)','Half Large Potato(75g)','Oats(250g)','2 corn tortillas']
    ps = ['Soy nuts(i Oz)','Low fat milk(250ml)','Hummus(4 Tbsp)','Cottage cheese (125g)','Flavored yogurt(125g)']
    taste_en = ['2 TSP (10 ml) olive oil','2 TBSP (30g) reduced-calorie salad dressin','1/4 medium avocado','Small handful of nuts','1/2 ounce  grated Parmesan cheese','1 TBSP (20g) jam, jelly, honey, syrup, sugar']

    cal=float(input("ENTER THE CALORIES BURNT: "));


    if cal<1500:
        print("Breakfast: "+protein[randint(0, 5)]+" + "+fruit[randint(0, 5)]);

        print("Lunch: "+protein[randint(0, 5)]+" + "+vegetable[0]+" + Leafy Greens"+grains[randint(0,4)]+" + "+taste_en[randint(0,5)]);

        print("Snack: "+ps[randint(0, 4)]+" + "+vegetable[0]);

        print("Dinner: "+protein[randint(0, 5)]+" + 2 "+vegetable[0]+" + Leafy Greens"+grains[randint(0,4)]+" + "+taste_en[randint(0,5)]);
            
        print("Snack: "+fruit[randint(0, 5)]);



    elif cal<1800:

        print("Breakfast: "+protein[randint(0, 5)]+" + "+fruit[randint(0, 5)])

        print("Lunch: "+protein[randint(0, 5)]+" + "+vegetable[0]+" + Leafy Greens"+grains[randint(0,4)]+" + "+taste_en[randint(0,5)]+" + "+fruit[randint(0, 5)])

        print("Snack: "+ps[randint(0, 4)]+" + "+vegetable[0])

        print("Dinner: 2 "+protein[randint(0, 5)]+" + "+vegetable[0]+" + Leafy Greens"+grains[randint(0,4)]+" + "+taste_en[randint(0,5)])

        print("Snack: "+fruit[randint(0, 5)])


    elif cal<2200:

        print("Breakfast: "+protein[randint(0, 5)]+" + "+fruit[randint(0, 5)])

        print("Lunch: "+protein[randint(0, 5)]+" + "+vegetable[0]+" + Leafy Greens"+grains[randint(0,4)]+" + "+taste_en[randint(0,5)]+" + "+fruit[randint(0, 5)])

        print("Snack: "+ps[randint(0, 4)]+" + "+vegetable[0])

        print("Dinner: 2 "+protein[randint(0, 5)]+" + 2 "+vegetable[0]+" + Leafy Greens"+grains[randint(0,4)]+" + "+taste_en[randint(0,5)])

        print("Snack: "+fruit[randint(0, 5)])



    elif cal>=2200:

        print("Breakfast: 2 "+protein[randint(0, 5)]+" + "+fruit[randint(0, 5)]+" + "+grains[randint(0,4)])

        print("Lunch: "+protein[randint(0, 5)]+" + "+vegetable[0]+" + Leafy Greens"+grains[randint(0,4)]+" + "+taste_en[randint(0,5)]+" + "+fruit[randint(0, 5)])

        print("Snack: "+ps[randint(0, 4)]+" + "+vegetable[0])

        print("Dinner: 2 "+protein[randint(0, 5)]+" + 2 "+vegetable[0]+" + Leafy Greens + 2 "+grains[randint(0,4)]+" + 2 "+taste_en[randint(0,5)])

        print("Snack: "+fruit[randint(0, 5)])
diet()
