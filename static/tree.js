function drawTree(data) {
    d3.select("svg").remove(); // Clear previous tree
  
    const dx = 20;
    const dy = 160;
  
    const treeLayout = d3.tree().nodeSize([dx, dy]);
    const root = d3.hierarchy(data);
    treeLayout(root);
  
    // Calculate vertical space needed
    let x0 = Infinity, x1 = -Infinity;
    root.each(d => {
      if (d.x < x0) x0 = d.x;
      if (d.x > x1) x1 = d.x;
    });
  
    const width = 800;
    const height = x1 - x0 + dx * 2;
  
    const svg = d3.select("#tree").append("svg")
      .attr("viewBox", [-dy / 2, x0 - dx, width, height])
      .style("font", "12px sans-serif");
  
    const g = svg.append("g");
  
    // Draw links
    g.append("g")
      .attr("fill", "none")
      .attr("stroke", "#ccc")
      .attr("stroke-width", 2)
      .selectAll("path")
      .data(root.links())
      .join("path")
      .attr("d", d3.linkHorizontal()
        .x(d => d.y)
        .y(d => d.x));
  
    // Draw nodes
    const node = g.append("g")
      .selectAll("g")
      .data(root.descendants())
      .join("g")
      .attr("transform", d => `translate(${d.y},${d.x})`);
  
    node.append("circle")
      .attr("r", 5)
      .attr("fill", "white");
  
    node.append("text")
      .attr("dy", "0.31em")
      .attr("x", d => d.children ? -8 : 8)
      .attr("text-anchor", d => d.children ? "end" : "start")
      .text(d => d.data.name)
      .style("fill", "white");
  }
  
  document.getElementById("courseForm").addEventListener("submit", function (e) {
    e.preventDefault();
    const courseCode = document.getElementById("courseInput").value.trim().toUpperCase();
    if (!courseCode) return;
  
    fetch(`/data/${courseCode}`)
      .then(res => res.json())
      .then(data => {
        if (data.error) {
          alert("Course not found.");
        } else {
          drawTree(data);
        }
      });
  });
  