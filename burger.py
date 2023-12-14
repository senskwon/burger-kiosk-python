from collections import deque

class BurgerKiosk:
    def __init__(self):
        self.orders_queue = deque()
        self.location = None
        self.all_orders = []
        self.total_price = 0

    def display_submenu(self, category, items, show_price=True):
        print(f"{category}를 선택하세요:")
        for index, item in enumerate(items, start=1):
            if show_price:
                print(f"{index}. {item} - {self.get_price(item)}원")
            else:
                print(f"{index}. {item}")

    def get_price(self, item):
        return {
            "와퍼": 5000,
            "통새우 와퍼": 5500,
            "콰트로 치즈 와퍼": 6000,
            "와퍼 주니어": 4000,
            "프렌치프라이": 2500,
            "치즈스틱": 3000,
            "너겟킹": 3500,
            "콜라": 1500,
            "사이다": 1500,
            "선택 안함": 0
        }[item]

    def take_location(self):
        self.display_submenu("장소", ["포장", "매장"], show_price=False)
        location_choice = input("장소 선택 (1-2): ")
        if location_choice.isdigit() and 1 <= int(location_choice) <= 2:
            self.location = ["포장", "매장"][int(location_choice) - 1]
        else:
            print("올바르지 않은 선택입니다. 프로그램을 종료합니다.")
            exit()

    def take_order(self):
        while True:
            order = {"장소": None, "햄버거": None, "사이드": None, "음료": None}

            if not self.location:
                self.take_location()
                order["장소"] = self.location

            self.display_submenu("햄버거", ["와퍼", "통새우 와퍼", "콰트로 치즈 와퍼", "와퍼 주니어"])
            burger_choice = input("햄버거 선택 (1-4): ")
            if burger_choice.isdigit() and 1 <= int(burger_choice) <= 4:
                order["햄버거"] = ["와퍼", "통새우 와퍼", "콰트로 치즈 와퍼", "와퍼 주니어"][int(burger_choice) - 1]
                order["금액"] = self.get_price(order["햄버거"])
                self.total_price += order["금액"]
            else:
                print("올바르지 않은 선택입니다. 주문이 취소됩니다.")
                return

            self.display_submenu("음료", ["콜라", "사이다", "선택 안함"])
            drink_choice = input("음료 선택 (1-3): ")
            if drink_choice.isdigit() and 1 <= int(drink_choice) <= 3:
                order["음료"] = ["콜라", "사이다", "선택 안함"][int(drink_choice) - 1]
                order["금액"] += self.get_price(order["음료"])
                self.total_price += self.get_price(order["음료"])
            else:
                print("올바르지 않은 선택입니다. 주문이 취소됩니다.")
                return

            self.display_submenu("사이드", ["프렌치프라이", "치즈스틱", "너겟킹", "선택 안함"])
            side_choice = input("사이드 선택 (1-4): ")
            if side_choice.isdigit() and 1 <= int(side_choice) <= 4:
                order["사이드"] = ["프렌치프라이", "치즈스틱", "너겟킹", "선택 안함"][int(side_choice) - 1]
                order["금액"] += self.get_price(order["사이드"])
                self.total_price += self.get_price(order["사이드"])
            else:
                print("올바르지 않은 선택입니다. 주문이 취소됩니다.")
                return

            self.all_orders.append(order)
            print("주문이 추가되었습니다.")

            continue_ordering = input("계속 주문하시겠습니까? (y/n): ")
            if continue_ordering.lower() != 'y':
                break

    def process_orders(self):
        print("주문 정보:")
        for index, order in enumerate(self.all_orders, start=1):
            print(f"{index}. "
                  f"햄버거: {order['햄버거']} - {self.get_price(order['햄버거'])}원, "
                  f"음료: {order['음료']} - {self.get_price(order['음료'])}원, "
                  f"사이드: {order['사이드']} - {self.get_price(order['사이드'])}원")

        print(f"\n총 주문 금액: {self.total_price}원")

kiosk = BurgerKiosk()

kiosk.take_order()
kiosk.process_orders()