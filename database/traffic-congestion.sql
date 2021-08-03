DROP schema IF EXISTS traffic;

CREATE SCHEMA traffic;
USE traffic;

create table traffic
(
	trafficId INT NOT NULL AUTO_INCREMENT,
    date_time datetime NOT NULL,
    traffic_flow INT NOT NULL,
    result varchar(50),
    
    PRIMARY KEY (trafficId)
);