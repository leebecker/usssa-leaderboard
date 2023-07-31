<template>
    <div class="divTableRow" :class="{divTableRowEven: isEvenRow}">
        <div class="divTableCell">{{standing.rank}}</div>
        <div class="divTableCell">{{contingent.name}}</div>
        <div class="divTableCell"><img :src="require(`@/assets/flags/84x63/${countryCodeLower}.png`)" :alt="contingent.country"></div>
        <div class="divTableCell">{{standing.gold}}</div>
        <div class="divTableCell">{{standing.silver}}</div>
        <div class="divTableCell">{{standing.bronze}}</div>
        <div class="divTableCell">{{standing.points}}</div>
    </div>
</template>


<script>

  export default {
    props: {
        "contingent": {
            type: Object
        },
        "standing": {
            type: Object
        },
        "rowIndex": {
            type: Number
        }

    },
    //props: ["rank", "name", "gold", "silver", "bronze", "points"],
    computed: {
        countryCodeLower() {
            return this.contingent.country.toLowerCase()
        },
        isEvenRow() {
            console.log(this)
            console.log("ROW ")
            console.log(this.rowIndex)
            return this.rowIndex % 2 == 0;
        }
    }
  };
</script>

<style scoped>
.divTableRow {
	display: table-row;
    background-color: #E0E0E0;
}

.divTableRowEven {
	display: table-row;
    background-color: #FFFFFF;
}

.divTableCell {
	border: 1px solid #999999;
	display: table-cell;
	padding: 3px 10px;
    font-size: x-large;
    vertical-align: middle;
}

.divTableFoot {
	background-color: #EEE;
	display: table-footer-group;
	font-weight: bold;
}

</style>