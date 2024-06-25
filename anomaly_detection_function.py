def anomaly_detection(row,time_threshold=3600,distance_threshold=100):
    if row['time_diff'] < time_threshold and row['geo_distance_diff'] > distance_threshold:
        return 1
    return 0
