CREATE TABLE IF NOT EXISTS vehicles
(
    "id" SERIAL NOT NULL,
    "track_id" TEXT NOT NULL,
    "lat" FLOAT NOT NULL,
    "lon" FLOAT DEFAULT NULL,
    "speed" FLOAT DEFAULT NULL,
    "lon_acc" FLOAT DEFAULT NULL,
    "lat_acc" FLOAT DEFAULT NULL,
    "time" FLOAT DEFAULT NULL,
    PRIMARY KEY ("id"),
    CONSTRAINT fk_trajectory
        FOREIGN KEY("track_id") 
            REFERENCES trajectories(track_id)
            ON DELETE CASCADE
    
);