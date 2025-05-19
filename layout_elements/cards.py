import dash_bootstrap_components as dbc


def create_card(header, element_id):
    return dbc.CardBody([
        dbc.CardHeader(header),
        dbc.Card(id=element_id, className='text-center text-success my-4')
    ])


# Task: Uniform looking cards in mobile view!
cars_sold_card = create_card('Cars Sold', 'cars-sold')
sales_sum_card = create_card('Total Sales', 'sum-sales')
best_model_card = create_card('Bestseller Model', 'best-model')
best_make_card = create_card('Bestseller Make', 'best-make')

test_card = create_card('Card for testing', 'test-card')
