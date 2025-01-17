from commands.comand_factory import CommandFactory

class AddDriver(CommandFactory):
    def execute(self):
        self.driver_service.add_driver()

class AddCar(CommandFactory):
    def execute(self):
        self.car_service.add_car()

class DeleteCar(CommandFactory):
    def execute(self):
        self.car_service.delete_car()

class ShowAllCars(CommandFactory):
    def execute(self):
        self.car_service.show_all_cars()

class DeleteDriver(CommandFactory):
    def execute(self):
        self.driver_service.delete_driver()

class ShowAllDrivers(CommandFactory):
    def execute(self):
        self.driver_service.show_all_drivers()

class ShowDriverById(CommandFactory):
    def execute(self):
        self.driver_service.show_driver_by_id()