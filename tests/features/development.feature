Feature: developer developing software

  Scenario: developer increases software completion by one
     Given we have a dev and an unfinished software
      When dev codes 1 unit
      Then software will complete 1 unit
