.PHONY: all clean

P4C:=p4c-bm2-ss

BLD=build
BLD_BMV2=$(BLD)/BMv2

TARGET=TARGET_BMV2

all: $(BLD_BMV2)/networks/ALV/ALV.json \
     $(BLD_BMV2)/networks/p4_tutorials/basic/basic.json \
     $(BLD_BMV2)/networks/p4_tutorials/basic_tunnel/basic_tunnel.json \
     $(BLD_BMV2)/networks/p4_tutorials/p4runtime/advanced_tunnel.json \
     $(BLD_BMV2)/networks/p4_tutorials/ecn/ecn.json \
     $(BLD_BMV2)/networks/p4_tutorials/mri/mri.json \
     $(BLD_BMV2)/networks/p4_tutorials/source_routing/source_routing.json \
     $(BLD_BMV2)/networks/p4_tutorials/calc/calc.json \
     $(BLD_BMV2)/networks/p4_tutorials/load_balance/load_balance.json \
     $(BLD_BMV2)/networks/p4_tutorials/qos/qos.json \
     $(BLD_BMV2)/networks/p4_tutorials/firewall/firewall.json \
     $(BLD_BMV2)/networks/p4_tutorials/link_monitor/link_monitor.json \
     $(BLD_BMV2)/networks/3net/3net.json \
     $(BLD_BMV2)/networks/midproject/midproject.json
clean:
        rm -fr $(BLD)

$(BLD_BMV2)/%.json: %.p4
        mkdir -p `dirname $@`
        $(P4C) --emit-externs -I lib $< -o $@ --target bmv2 --arch v1model -DTARGET_BMV2