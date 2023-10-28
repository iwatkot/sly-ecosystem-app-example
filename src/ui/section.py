from supervisely.app.widgets import Card, Button, Flexbox, InputNumber, Select


lock_card_button = Button("Lock card")
lock_card_button.hide()
unlock_card_button = Button("Unlock card")
buttons_flexbox = Flexbox([lock_card_button, unlock_card_button])

left_number_input = InputNumber(min=1, max=10, size="medium")
right_number_input = InputNumber(min=1, max=10, size="medium")

operator_select = Select(
    [Select.Item("+"), Select.Item("-"), Select.Item("*"), Select.Item("/")]
)

result_input = InputNumber(controls=False, size="medium")
result_input.disable()

calculator_flexbox = Flexbox(
    [left_number_input, operator_select, right_number_input, result_input]
)


card = Card(
    title="Hello, Supervisely!",
    description="Simple calculator.",
    content=calculator_flexbox,
    collapsable=True,
    content_top_right=buttons_flexbox,
    lock_message="Press Unlock card button!",
)
card.collapse()
card.lock()


@unlock_card_button.click
def unlock_card():
    card.unlock()
    card.uncollapse()
    lock_card_button.show()
    unlock_card_button.hide()


@lock_card_button.click
def lock_card():
    card.lock()
    lock_card_button.hide()
    unlock_card_button.show()


def calculate(_):
    left_number = left_number_input.get_value()
    right_number = right_number_input.get_value()

    operator = operator_select.get_value()
    result = eval(f"{left_number} {operator} {right_number}")

    result_input.value = result


left_number_input.value_changed(calculate)
right_number_input.value_changed(calculate)
operator_select.value_changed(calculate)
