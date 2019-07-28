queue()
    .defer(d3.json, "canada_climate")
    .defer(d3.json, "static/visualapp/geojson/canada.json")
    .await(makeGraphs);

function makeGraphs(error, projectsJson, statesJson) {

    //Clean projectsJson data
    var donorschooseProjects = projectsJson;
    console.log(projectsJson)
    var dateFormat = d3.time.format("%Y-%m-%d");
    donorschooseProjects.forEach(function (d) {    
        d["yearmon"] = dateFormat.parse(d["yearmon"]);
        console.log(d["yearmon"]);
       // d["yearmon"].setDate(1);
        d["total_precip"] = +d["total_precip"];
    });


    //Create a Crossfilter instance
    var ndx = crossfilter(donorschooseProjects);    

    //Define Dimensions
    var dateDim = ndx.dimension(function (d) { return d["yearmon"]; });
    console.log("Dates"+dateDim);
    var resourceTypeDim = ndx.dimension(function (d) { return d["province"]; });
    var povertyLevelDim = ndx.dimension(function (d) { return d["province"]; });
    var stateDim = ndx.dimension(function (d) { return d["province"]; });
    var totalDonationsDim = ndx.dimension(function (d) { return d["total_precip"]; });
    console.log("go crazy 5");

    //Calculate metrics
    var numProjectsByDate = dateDim.group();
    var numProjectsByResourceType = resourceTypeDim.group();
    var numProjectsByPovertyLevel = povertyLevelDim.group();
    var totalDonationsByState = stateDim.group().reduceSum(function (d) {
        return d["total_precip"];
    });
    console.log("go crazy 6");

    var all = ndx.groupAll();
    var totalDonations = ndx.groupAll().reduceSum(function (d) { return d["total_precip"]; });

    var max_state = totalDonationsByState.top(1)[0].value;

    console.log("go crazy 7");
    //Define values (to be used in charts)
    var minDate = dateDim.bottom(1)[0]["yearmon"];
    var maxDate = dateDim.top(1)[0]["yearmon"];
    //Charts
    var timeChart = dc.barChart("#time-chart");
    var resourceTypeChart = dc.rowChart("#resource-type-row-chart");
    var povertyLevelChart = dc.rowChart("#poverty-level-row-chart");
    var usChart = dc.geoChoroplethChart("#us-chart");
    var numberProjectsND = dc.numberDisplay("#number-projects-nd");
    var totalDonationsND = dc.numberDisplay("#total-donations-nd");

    numberProjectsND
        .formatNumber(d3.format("d"))
        .valueAccessor(function (d) { return d; })
        .group(all);

    totalDonationsND
        .formatNumber(d3.format("d"))
        .valueAccessor(function (d) { return d; })
        .group(totalDonations)
        .formatNumber(d3.format(".3s"));

    timeChart
        .width(600)
        .height(160)
        .margins({ top: 10, right: 50, bottom: 30, left: 50 })
        .dimension(dateDim)
        .group(numProjectsByDate)
        .transitionDuration(500)
        .x(d3.time.scale().domain([minDate, maxDate]))
        .elasticY(true)
        .xAxisLabel("Year")
        .yAxis().ticks(4);

    resourceTypeChart
        .width(300)
        .height(250)
        .dimension(resourceTypeDim)
        .group(numProjectsByResourceType)
        .xAxis().ticks(4);

    povertyLevelChart
        .width(300)
        .height(250)
        .dimension(povertyLevelDim)
        .group(numProjectsByPovertyLevel)
        .xAxis().ticks(4);

    usChart.width(1000)
        .height(400)
        .dimension(stateDim)
        .group(totalDonationsByState)
        .colors(["#E2F2FF", "#C4E4FF", "#9ED2FF", "#81C5FF", "#6BBAFF", "#51AEFF", "#36A2FF", "#1E96FF", "#0089FF", "#0061B5"])
        .colorDomain([0, max_state])
        .overlayGeoJson(statesJson["features"], "state", function (d) {
            return d.properties.name;
        }).projection(d3.geo.albers()
            .scale(600).center([0,60])
            .translate([400, 200]))
        .title(function (p) {
            return "State: " + p["key"]
                + "\n"
                + "Total Donations: " + Math.round(p["value"]) + " $";
        })

    console.log("go crazy 15");
    dc.renderAll();
    console.log("go crazy 16");

};