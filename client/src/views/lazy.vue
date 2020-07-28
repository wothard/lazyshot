<template>
  <div class="root">
    <div>
      <button @click.ctrl="shifd()">显示</button>
      <button @click.alt="hideds()">隐藏</button>
    </div>
    <div class="table-box">
      <div class="table-list-choice">
        <div
          :key="index"
          @click="pickTables(item)"
          class="choice-item"
          v-for="(item, index) in backendTableLists"
        >
          <img src="../assets/svg/cereal-table-svgrepo-com.svg" />
          <span>{{ item.name }}</span>
        </div>
      </div>
      <!-- table info, for list -->
      <div class="table-content">
        <div :key="index" class="table-item" v-for="(item, index) in activeTableLists">
          <div class="table-name">
            <div class="name-point"></div>
            <span>{{item.name}}</span>
          </div>
          <div
            :class="pickUp.name === (item.name + structDetail.name) ? 'choice-color' : 'default-color'"
            :id="item.name + structDetail.name"
            :key="indexStruct"
            @click="
              setLineToConnect(item.name + structDetail.name, item.name, $event)
            "
            class="table-key-box"
            v-for="(structDetail, indexStruct) in item.struct"
          >{{ structDetail.name }}</div>
          <!-- @="setLineToRemove('table-one' + item)" -->
        </div>
      </div>

      <!-- <div class="table-item">
        <div
          :id="'table-two'+ item"
          class="table-key-box"
          :class="pickUp == ('table-two'+ item)?'choice-color':'default-color'"
          v-for="item in 10"
          :key="item"
          @click="setLineToConnect('table-two' + item, $event)"
        >fsadfd343sa</div>
      </div>-->
    </div>
  </div>
</template>

<script>
import LeaderLine from 'leader-line-vue'
import { getDBList } from '@/api/index'
export default {
  name: 'Lazy',
  data() {
    return {
      backendTableLists: [],
      activeTableLists: [],
      activeTableNameLists: [],
      isSameTableFeild: '', // 是否两次选中同一个表
      line: LeaderLine,
      shitLine: undefined,
      shit: 0,
      lineObjList: {},
      tempSetPoint: {
        startElement: undefined,
        endElement: undefined
      },
      tempRemovePoint: 0,
      tempRemovePointName: '',
      pickUp: {
        name: '',
        count: 0
      },
      colorList: [
        'rgba(30, 130, 250, 0.5)',
        'rgba(253, 121, 168, 0.5)',
        'rgba(0, 184, 148, 0.5)',
        'rgba(162, 155, 254,0.5)',
        'rgba(250, 177, 160,0.5)',
        'rgba(99, 110, 114,0.5)',
        'rgba(232, 67, 147,0.5)',
        'rgba(186, 220, 88,0.5)',
        'rgba(106, 176, 76,0.5)',
        'rgba(19, 15, 64,0.5)',
        'rgba(235, 77, 75,0.5)',
        'rgba(255, 192, 72,0.5)',
        'rgba(30, 39, 46,0.5)',
        'rgba(15, 188, 249,0.5)',
        'rgba(60, 64, 198,0.5)',
        'rgba(255, 221, 89,0.5)',
        'rgba(245, 59, 87,0.5)',
        'rgba(24,255,255 ,0.5)',
        'rgba(255,179,0 ,0.5)',
        'rgba(229,115,115 ,0.5)',
        'rgba(156,39,176 ,0.5)',
        'rgba(124,77,255 ,0.5)',
        'rgba(129,212,250 ,0.5)',
        'rgba(0,137,123 ,0.5)',
        'rgba(121,85,72 ,0.5)',
        'rgba(3,155,229 ,0.5)',
        'rgba(44, 44, 84,0.5)',
        'rgba(112, 111, 211,0.5)',
        'rgba(170, 166, 157,0.5)',
        'rgba(71, 71, 135,0.5)',
        'rgba(204, 142, 53,0.5)',
        'rgba(179, 57, 57,0.5)',
        'rgba(46, 213, 115,0.5)',
        'rgba(55, 66, 250,0.5)'
      ]
    }
  },
  created() {
    // console.log(LeaderLine)
    // this.$toastr.s('SUCCESS MESSAGE', 'Success Toast Title')
    // console.log(this.$toastr)
    this.initTables()
    //   LeaderLine.setLine(this.$refs.start, this.$refs.end);
  },
  methods: {
    initTables() {
      getDBList().then((response) => {
        this.backendTableLists = response.data
      })
    },
    // 控制显示表
    pickTables(q) {
      const spliceIndex = this.activeTableNameLists.indexOf(q.name)
      if (spliceIndex !== -1) {
        this.activeTableLists.splice(spliceIndex, 1)
        this.activeTableNameLists.splice(spliceIndex, 1)
      } else {
        this.activeTableLists.push(q)
        this.activeTableNameLists.push(q.name)
      }
    },
    setLij() {
      this.shitLine = this.line.setLine(
        document.getElementById('start'),
        document.getElementById('end'),
        { hide: true }
      )
      console.log(this.shitLine, '---')
      this.shit += 1
      if (this.shit === 3) {
        this.line.remove()
      }
    },
    setLineToConnect(name, pname, ent) {
      this.checkPicked(name)
      if (this.checkSameTable(pname)) {
        this.isSameTableFeild = ''
        this.tempSetPoint = {
          startElement: undefined,
          endElement: undefined
        }
        this.$toastr.w('WARN', '暂不支持表内自连接')
        return
      }
      // this.checkSameTable(pname)
      // const ds = this.checkClickType(ent)
      // console.log(ds)
      if (this.tempSetPoint.start === undefined) {
        this.tempSetPoint.start = name
      } else {
        this.tempSetPoint.end = name
        console.log(this.tempSetPoint)
        var cocolor = this.colorList
        const currentLine = LeaderLine.setLine(
          document.getElementById(this.tempSetPoint.start),
          document.getElementById(this.tempSetPoint.end),
          {
            hide: false,
            dash: { animation: true },
            color: cocolor[Math.floor(Math.random() * cocolor.length)],
            endPlug: 'arrow3'
          }
        )
        this.lineObjList[
          this.tempSetPoint.start + this.tempSetPoint.end
        ] = currentLine
        this.tempSetPoint = {
          startElement: undefined,
          endElement: undefined
        }
      }
    },
    setLineToRemove(e) {
      console.log(e)
      this.tempRemovePointName += e
      this.tempRemovePoint += 1
      if (this.tempRemovePoint === 2) {
        if (
          Object.prototype.hasOwnProperty.call(
            this.lineObjList,
            this.tempRemovePointNam
          )
        ) {
          this.lineObjList[this.tempRemovePointName].remove()
        }
        this.tempRemovePointName = ''
        this.tempRemovePoint = 0
      }
    },
    shifd() {
      this.shitLine.show()
    },
    hideds() {
      this.shitLine.hide()
    },
    checkClickType(e) {
      if (e.altKey && e.shiftKey) {
        return 'inner'
      } else if (e.altKey && !e.shiftKey) {
        return 'left'
      } else if (!e.altKey && e.shiftKey) {
        return 'right'
      } else {
        return 'none'
      }
    },
    // 控制选中表格colum
    checkPicked(name) {
      this.pickUp.name = name
      this.pickUp.count += 1
      if (this.pickUp.count === 2) {
        setTimeout(() => {
          this.pickUp = {
            name: '',
            count: 0
          }
        }, 400)
      }
    },
    // 判断是否选中同一个表
    checkSameTable(pname) {
      console.log(this.isSameTableFeild, '0000>>', pname)
      if (this.isSameTableFeild === pname) {
        return true
      } else {
        this.isSameTableFeild = pname
        return false
      }
    }
  }
}
</script>

<style lang="scss" scoped>
.root {
  background-color: #fafafa;
  display: flex;
  flex-direction: column;
  align-items: center;
}
.io {
  position: relative;
  top: 100px;
  right: 300px;
}
.table-box {
  width: 90vw;
  box-sizing: border-box;
  background-color: #f3f2ef;
  padding: 10px;
  min-height: 80vh;
  border-radius: 5px;
  box-shadow: 0 5px 20px rgba(0, 0, 0, 0.19);
  display: flex;
  flex-wrap: wrap;
  .table-list-choice {
    height: 100%;
    background: #fff;
    box-shadow: 0 6px 8px rgba(85, 102, 119, 0.03),
      0 1px 1px rgba(85, 102, 119, 0.8);
    margin-right: 20px;
    .choice-item {
      cursor: pointer;
      padding: 5px;
      border-top: solid 1px rgba(85, 102, 119, 0.18);
      display: flex;
      align-items: center;
      img {
        width: 46px;
        height: 46px;
      }
      span {
        padding-left: 10px;
        font-size: 20px;
        min-width: 80px;
      }
    }
  }
  .table-content {
    display: flex;
    flex-wrap: wrap;
    .table-item {
      padding: 10px;
      min-width: 120px;
      box-shadow: 0 8px 33px 0 rgba(30, 35, 42, 0.16);
      border-radius: 4px;
      margin-right: 90px;
      margin-bottom: 50px;
      .table-key-box {
        cursor: pointer;
        margin: 8px 0;
        padding: 4px;
        border: 1px solid transparent;
        border-radius: 0.25rem;
      }
      .table-name {
        width: 100%;
        display: flex;
        align-items: center;
        justify-content: center;
        .name-point {
          margin-right: 10px;
          width: 8px;
          height: 8px;
          background: #77dab2;
          border-radius: 50%;
        }
        span {
          font-weight: bold;
          font-size: 26px;
        }
      }
    }
  }
}
.default-color {
  color: #333333;
  background-color: #e1e3e4;
}
.choice-color {
  color: #ffffff;
  background-color: #2f6bdb;
}
</style>
