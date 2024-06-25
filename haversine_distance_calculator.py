def calculateDistance(row):
    transaction_coords = (row['lat'] , row['long'])
    merchants_coords = (row['merch_lat'] , row['merch_long'])
    return geodesic(transaction_coords,merchants_coords)
