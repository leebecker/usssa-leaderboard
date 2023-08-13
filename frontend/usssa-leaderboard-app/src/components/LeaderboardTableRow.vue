<template>
    <div class="divTableRow" :class="{divTableRowEven: isEvenRow}">
        <div class="divTableCell">{{standing.rank}}</div>
        <div class="divTableCellContingent">{{contingent.name}}</div>
        <div class="divTableCell">
            <img v-if="isValidCountry" :src="require(`@/assets/flags/84x63/${countryCodeLower}.png`)" :alt="contingent.country" class="fullImg">
            <span v-else class="fullImg"> -- </span>
            <img v-if="isValidCountry" :src="require(`@/assets/flags/84x63/${countryCodeLower}.png`)" :alt="contingent.country" class="smallImg">
            <span v-else class="smallImg"> -- </span>
        </div>
        <div class="divTableCell">{{standing.gold}}</div>
        <div class="divTableCell">{{standing.silver}}</div>
        <div class="divTableCell">{{standing.bronze}}</div>
        <div class="divTableCell">{{standing.medals}}</div>
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
        isValidCountry() {
            return this.contingent.is_national_federation
        },
        isEvenRow() {
            return this.rowIndex % 2 == 0;
        }
    }
  };
</script>

<style scoped>
.divTableRow {
	display: table-row;
    background-color: #E0E0E0;
    /*height: 80px;*/
}

.divTableRowEven {
	display: table-row;
    background-color: #FFFFFF;
    /*height: 80px;*/
}

.divTableCell {
	border: 1px solid #999999;
	display: table-cell;
	padding: 0px 0px;
    vertical-align: middle;
}

.divTableCellContingent {
	border: 1px solid #999999;
	display: table-cell;
	padding: 0px 5px;
    vertical-align: middle;
    text-align: left;
}


.divTableFoot {
	background-color: #EEE;
	display: table-footer-group;
	font-weight: bold;
}

.fullImg {
    display: inline;
      transform: scale(0.5, 0.5);
}
.smallImg {
    display: none;
      transform: scale(0.25, 0.25);

}

@media screen and (max-width: 500px) {
    .fullImg {
      display: none;
      transform: scale(0.5, 0.5);
    }
    .smallImg {
      display: inline;
      transform: scale(0.25, 0.25);
    }
}

</style>