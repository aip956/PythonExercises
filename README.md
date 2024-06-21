# Welcome to Eng Lab 4, Event-Driven Microservice


## Task

## Description


## Pieces

### Flow
#### Task Assignment
    Coordinator (Producer) receives event
    Coordinator publishes to the Organizer (Broker)
    Worker (Consumer) subscribes to event
    Worker receives event
    Worker service updates the database and acknowledges event

#### Notification
    Coordinator generates a "Notification" event
    Producer service publishes event to the Broker
    Notification service subscribes to "Notification" events
    Notification service receives the event and sends a notification
    Notification service updates the database and acknowledges the event

####


## Installation

## Usage