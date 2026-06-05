Feature: ParkingUV parking fee calculation
  As a parking lot customer
  I want the system to calculate my fee based on my stay duration and membership
  So that I know exactly how much to pay when leaving

  Scenario: Parking for less than 30 minutes
    Given a standard customer parks their vehicle
    When the parking duration is 30 minutes
    Then the total fee should be 0 pesos

  Scenario: Hourly charge after the grace period
    Given a standard customer parks their vehicle
    When the parking duration is 65 minutes
    Then the total fee should be 1000 pesos

  Scenario: VIP discount application
    Given a VIP customer parks their vehicle
    When the parking duration is 60 minutes
    Then the total fee should be 400 pesos

  Scenario: Daily maximum cap
    Given a standard customer parks their vehicle
    When the parking duration is 1500 minutes
    Then the total fee should be 12000 pesos