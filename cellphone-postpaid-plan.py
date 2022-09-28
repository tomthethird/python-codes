call = int(input())
text = int(input())
FEE = 25.00

if call > 60:
    call_excess = (call - 60) * 6.5
else:
    call_excess = 0

if text > 100:
    text_excess = text - 100
else:
    text_excess = 0

bill = 799 + 25 + call_excess + text_excess
tax = bill * 0.05

bill += tax

print(f"Call minutes: {call:.1f}")
print(f"Text messages: {text:.1f}")
print(f"Excess minute charges: {call_excess:.2f}")
print(f"Excess SMS charges: {text_excess:.2f}")
print(f"911 fee: {FEE}")
print(f"Tax: {tax:.2f}")
print(f"Total bill: {bill:.2f}")