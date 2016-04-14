*** Settings ***
Library    verify_payment.PaymentVerifier
*** Test Cases ***
Test Payment
    [Documentation]    Author: Bartosz Koperek
    ...    This test automates a booking up to a declined payment and verifies the payment result.
    ...    The test is passed if payment declined message is found.
    ...    Requirements: date format: DD/MM/YYYY, card expiration date format: MM/YYYY, correct credit card number

    Given I make a booking from 'DUB' to 'SXF' on '16/05/2016' for '2' adults and '1' child
    When I pay for booking with card details '5555 5555 5555 5557', '10/2018' and '265'
    Then I should get payment declined message

*** Keywords ***
I make a booking from '${flight_from}' to '${flight_to}' on '${flight_date}' for '${adults_number}' adults and '${children_number}' child
    verify_payment.PaymentVerifier.fill_in_flight_details    ${flight_from}    ${flight_to}    ${flight_date}    ${adults_number}    ${children_number}
I pay for booking with card details '${card_number}', '${card_expiration_date}' and '${card_cvv}'
    verify_payment.PaymentVerifier.provide_payment_details    ${card_number}    ${card_expiration_date}    ${card_cvv}
I should get payment declined message
    verify_payment.PaymentVerifier.check_payment_result