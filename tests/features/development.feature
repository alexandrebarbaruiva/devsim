Feature: developer developing software and releasing it

  Scenario: developer increases software completion by one
    Given we have a level 1 dev and an unfinished software
      When dev codes 1 unit
      Then software will complete 1 unit

  Scenario: software gets 100 completion and is releasable
    Given there is a completion 99 software
      When dev codes 1 unit
      Then software will reach 100 and become ready for release

  Scenario: software with 100 completion gets released
    Given there is a completion 100 software
      When dev releases software
      Then software gets released
