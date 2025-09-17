def in_autotests_we_trust(a, b):
    if a == b:
        print('PASS')
    else:
        print('FAIL')

in_autotests_we_trust(10, '10')

in_autotests_we_trust(0, False)
in_autotests_we_trust(1, False)
in_autotests_we_trust(20, '220')
in_autotests_we_trust(20, '20')
