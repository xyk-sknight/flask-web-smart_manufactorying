import serial
import time
import modbus_tk
import modbus_tk.defines as cst
from modbus_tk import modbus_rtu
#主机端口
PORT = "COM1"


def main():
    """main"""
    logger = modbus_tk.utils.create_logger("console")

    try:
        # Connect to the slave
        master = modbus_rtu.RtuMaster(
            serial.Serial(port=PORT, baudrate=9600, bytesize=8, parity='N', stopbits=1, xonxoff=0)
        )
        master.set_timeout(3.0)
        master.set_verbose(True)
        logger.info("connected")
        while 1:
            # 读保持寄存器
            registers = master.execute(1, cst.READ_HOLDING_REGISTERS, 40000,10)
            print(registers)
            time.sleep(5)


    except modbus_tk.modbus.ModbusError as exc:
        logger.error("%s- Code=%d", exc, exc.get_exception_code())
def read():
    try:
        # Connect to the slave
        master = modbus_rtu.RtuMaster(
            serial.Serial(port=PORT, baudrate=9600, bytesize=8, parity='N', stopbits=1, xonxoff=0)
        )
        master.set_timeout(3.0)
        master.set_verbose(True)
        # 读保持寄存器
        registers = master.execute(1, cst.READ_HOLDING_REGISTERS, 40000,10)
        return registers
    except modbus_tk.modbus.ModbusError as exc:
        print("%s- Code=%d", exc, exc.get_exception_code())

def write():
    try:
        # Connect to the slave
        master = modbus_rtu.RtuMaster(
            serial.Serial(port=PORT, baudrate=9600, bytesize=8, parity='N', stopbits=1, xonxoff=0)
        )
        master.set_timeout(3.0)
        master.set_verbose(True)
        # 写寄存器起始地址为0的保持寄存器，操作寄存器个数为4
        master.execute(1, cst.WRITE_MULTIPLE_REGISTERS, 40000, output_value=[2000, 4000, 1])
    except modbus_tk.modbus.ModbusError as exc:
        print("%s- Code=%d", exc, exc.get_exception_code())
if __name__ == "__main__":
    write()