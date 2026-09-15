import re

# Let's craft the exact calibrated sections

intro = """
      <!-- Introduction -->
      <section>
        <p style="font-size: 1.15rem; line-height: 1.8; color: var(--color-text);">
          When twilight blankets the Appalachian ridgelines of Sullivan County, Tennessee, and stadium floodlights illuminate <strong>"The Last Great Colosseum,"</strong> a legendary aroma drifts across the hills. It is the perfume of cured hickory embers, slow-smoked pork fat, caramelized brown sugar, and tangy apple cider mop sauce. At Bristol Motor Speedway, the high-octane racing on the world's most feared 0.533-mile concrete oval is only half the thrill. The other half unfolds outdoors around glowing charcoal kettles, pellet smokers, and loaded camp tables.
        </p>
        <p>
          Whether you are an experienced pitmaster hauling an offset smoker or an RV camper firing up a portable griddle, an authentic <strong>Bristol Motor Speedway tailgate</strong> is an essential motorsport ritual. This definitive <strong>NASCAR tailgate guide</strong> gives you everything needed to conquer your <strong>race weekend BBQ camping Bristol</strong> getaway—from grill selection and five championship pit recipes to gear checklists, speedway cooler policies, and the electric energy of a <strong>Bristol race night party</strong> under the mountain stars.
        </p>
      </section>
"""

sec1_culture = """
      <!-- Section 1: The Legendary Bristol Tailgate Culture -->
      <section style="margin-top: 2.5rem;">
        <h2>🏁 The Legendary Bristol Tailgate Culture: Why It's the Best in NASCAR</h2>
        <p>
          Tailgating happens at every racetrack, but Bristol's culture is celebrated as the undisputed gold standard in NASCAR. What makes Thunder Valley so special? It starts with the dramatic Appalachian topography. Unlike superspeedways situated on vast, flat plains, Bristol Motor Speedway sits carved directly into a natural mountain bowl. That bowl architecture concentrates the celebration: laughter, bluegrass tunes, revving engines, and fragrant wood smoke rise together up the surrounding ridges.
        </p>
        <p>
          Bristol race fans do not simply tailgate for an hour or two before the green flag; they settle in for a multi-day outdoor festival spanning Thursday through Sunday. Rivalries are fierce on the high banks—whether your loyalty belongs to Kyle Larson, Chase Elliott, Denny Hamlin, or Ryan Blaney—yet the moment you enter the campground, friendly mountain hospitality takes over.
        </p>
        <div class="quote-box">
          &ldquo;Walk down any row of campers at Bristol and you will be greeted like family. Fans trade spare cold drinks for smoked sausages, lend extra tools, and invite strangers to pull up a lawn chair by the fire.&rdquo;
        </div>
        <p>
          The tailgate experience adapts to both hallmark speedway events. The daytime <a href="../food-city-500.html"><strong>Food City 500</strong></a> in April brings crisp spring breezes, morning skillet hash, and sunlit cookouts beneath blooming dogwood trees. Meanwhile, the September <a href="../bass-pro-night-race.html"><strong>Bass Pro Shops Night Race</strong></a> serves as the Cup Series Playoff cutoff, creating an electric festival atmosphere where smokers run all night and celebration continues long past the checkered flag.
        </p>
      </section>
"""

sec2_setup = """
      <!-- Section 2: BBQ Setup Guide -->
      <section style="margin-top: 2.5rem;">
        <h2>🔥 BBQ Setup Guide: What Grill to Bring to Your Campsite</h2>
        <p>
          Executing great barbecue at a campsite requires matching your cooking style with campground realities. Different cookers provide distinct advantages depending on your setup:
        </p>

        <div class="gear-grid">
          <div class="gear-card">
            <h4>🍖 Pellet Smokers (Traeger, Green Mountain)</h4>
            <p><strong>Best For:</strong> Reliable set-and-forget temperature control while you explore the Fan Zone.</p>
            <ul>
              <li><strong>Pros:</strong> Digital thermostat holds 225°F for 12 straight hours; clean hardwood smoke profile.</li>
              <li><strong>Requirement:</strong> Needs 110V power; full RV electric hookups make running pellet grills effortless.</li>
              <li><strong>Tip:</strong> Store pellets in sealed waterproof buckets to protect them from humid mountain air.</li>
            </ul>
          </div>

          <div class="gear-card">
            <h4>🪵 Charcoal Smokers &amp; Kettles (Weber, WSM)</h4>
            <p><strong>Best For:</strong> Pitmasters demanding heavy smoke rings and classic charcoal crust.</p>
            <ul>
              <li><strong>Pros:</strong> Unbeatable wood-fired bark; operates anywhere without electric utility connections.</li>
              <li><strong>Cons:</strong> Demands active airflow adjustment and mindful ash disposal.</li>
              <li><strong>Tip:</strong> Bring a galvanized steel bucket with a tight lid for safely cooling used charcoal ash.</li>
            </ul>
          </div>

          <div class="gear-card">
            <h4>🍳 Portable Propane Griddles (Blackstone 22")</h4>
            <p><strong>Best For:</strong> High-speed cooking, hearty breakfasts, and quick pre-race meals.</p>
            <ul>
              <li><strong>Pros:</strong> Instant heat with zero ash; ideal for morning smashburgers, eggs, bacon, and cheesesteaks.</li>
              <li><strong>Cons:</strong> Cannot produce low-and-slow wood smoke flavor.</li>
              <li><strong>Tip:</strong> Bring a conversion hose to run your tabletop griddle off a standard 20-lb propane tank.</li>
            </ul>
          </div>
        </div>

        <div class="callout-box">
          <h3>⚠️ Campsite Grilling Safety &amp; Etiquette</h3>
          <p style="margin-bottom: 0;">
            Always set your grill or smoker on flat, stable ground at least 10 feet away from camper canvas awnings, nylon tents, and RV slide-outs. Ridge winds can carry sparks, so never leave open coals unattended and keep an ABC-rated fire extinguisher or water bucket nearby.
          </p>
        </div>
      </section>
"""

mention1 = """
      <!-- Mention 1 with Phone CTA -->
      <div class="cta-inline">
        <p><strong>Planning to smoke your own brisket or ribs on race weekend?</strong> Reserve a spacious full hookup RV site with 30/50-amp power at Bristol Hilltop Camping by calling <a href="tel:+14233835373" style="color: var(--color-accent-light); font-weight: 700;">(423) 383-5373</a>.</p>
      </div>
"""

sec3_recipes = """
      <!-- Section 3: Top 5 Race Weekend BBQ Recipes -->
      <section style="margin-top: 2.5rem;">
        <h2>🏆 Top 5 Race Weekend BBQ Recipes for Bristol Campers</h2>
        <p>
          A memorable race day feast requires reliable recipes that can handle campsite prep schedules. These five fan-favorite dishes deliver championship flavor with manageable effort:
        </p>

        <!-- Recipe 1 -->
        <div class="recipe-card">
          <h3>1. Colosseum Pulled Pork Butt (Hickory Smoked Pork)</h3>
          <div class="recipe-meta">
            <span><strong>Prep:</strong> 15 Mins</span>
            <span><strong>Smoke Time:</strong> 8–10 Hours</span>
            <span><strong>Cook Temp:</strong> 225°F–250°F</span>
            <span><strong>Yield:</strong> 12–15 Servings</span>
          </div>
          <p>
            Bone-in pork shoulder (Boston butt) is the ultimate race weekend centerpiece because it is forgiving, yields massive portions, and holds hot for hours in an insulated cooler.
          </p>
          <p><strong>Key Ingredients:</strong> 1 (8–9 lb) bone-in pork butt, yellow mustard binder, sweet brown-sugar rub (paprika, black pepper, garlic powder, kosher salt, brown sugar), and a 50/50 apple cider vinegar spritz.</p>
          <p><strong>Method:</strong> Coat pork with mustard and rub. Smoke over hickory wood at 225°F for 5 hours until a mahogany bark develops. Spritz with cider mixture, wrap tightly in foil or butcher paper with brown sugar and butter, and cook at 250°F until probe-tender (203°F). Rest wrapped inside a dry cooler for 2 hours before pulling onto brioche buns with vinegar slaw.</p>
        </div>

        <!-- Recipe 2 -->
        <div class="recipe-card">
          <h3>2. Thunder Valley Smoked St. Louis Ribs (3-2-1 Method)</h3>
          <div class="recipe-meta">
            <span><strong>Prep:</strong> 15 Mins</span>
            <span><strong>Smoke Time:</strong> 6 Hours</span>
            <span><strong>Cook Temp:</strong> 225°F</span>
            <span><strong>Yield:</strong> 4–6 Servings</span>
          </div>
          <p>
            Tender spare ribs with a sweet, caramelized crust that yield clean, tender bites off the bone without turning mushy.
          </p>
          <p><strong>Key Ingredients:</strong> 2 racks St. Louis-cut pork spare ribs, barbecue pork rub, 4 tbsp butter, 1/4 cup brown sugar, 2 tbsp honey, and 1 cup sweet barbecue sauce.</p>
          <p><strong>Method:</strong> Season ribs generously. Smoke meat-side up at 225°F with applewood for 3 hours. Wrap tightly in heavy foil with butter, brown sugar, and honey, cooking 2 hours to tenderize. Unwrap, brush with sweet sauce, and cook 1 final hour until the glaze caramelizes. Slice between bones and serve immediately.</p>
        </div>

        <!-- Recipe 3 -->
        <div class="recipe-card">
          <h3>3. Overnight Brisket Sliders with Pickled Jalapeño Slaw</h3>
          <div class="recipe-meta">
            <span><strong>Prep:</strong> 20 Mins</span>
            <span><strong>Smoke Time:</strong> 12–14 Hours</span>
            <span><strong>Cook Temp:</strong> 225°F–250°F</span>
            <span><strong>Yield:</strong> 16–20 Sliders</span>
          </div>
          <p>
            Slow-smoked beef brisket on sweet rolls creates an irresistible aroma that attracts neighbors across the campground.
          </p>
          <p><strong>Key Ingredients:</strong> 1 whole packer USDA Prime beef brisket, coarse salt and black pepper (equal parts), Hawaiian sweet rolls, pickled sliced jalapeños, and tangy coleslaw.</p>
          <p><strong>Method:</strong> Season brisket with salt and pepper. Smoke overnight at 225°F using oak or hickory wood. When the internal stall hits (~165°F), wrap tightly in pink butcher paper and continue smoking at 250°F until tender at 202°F. Hold in a towel-lined cooler for 2 to 3 hours. Slice against the grain into thin ribbons and serve on sweet buns topped with slaw and jalapeños.</p>
        </div>

        <!-- Recipe 4 -->
        <div class="recipe-card">
          <h3>4. High-Banked Smoked &amp; Crisped Wings (Alabama White &amp; Buffalo)</h3>
          <div class="recipe-meta">
            <span><strong>Prep:</strong> 10 Mins</span>
            <span><strong>Cook Time:</strong> 1.5 Hours</span>
            <span><strong>Cook Temp:</strong> 250°F then 400°F</span>
            <span><strong>Yield:</strong> 6–8 Servings</span>
          </div>
          <p>
            Dry-brining with baking powder ensures bite-through crispy skin while infusing succulent wood smoke into every wing.
          </p>
          <p><strong>Key Ingredients:</strong> 4 lbs chicken wings (patted dry), 1 tbsp aluminum-free baking powder, 2 tbsp poultry rub, hot Buffalo sauce, and tangy Alabama white barbecue sauce (mayo, vinegar, pepper, horseradish).</p>
          <p><strong>Method:</strong> Toss dried wings with baking powder and rub. Smoke at 250°F for 45 minutes to absorb wood flavor. Crank grill to 400°F for 30 minutes, flipping once to crisp the skin. Toss half in spicy Buffalo and dunk the other half in Alabama white sauce for a two-flavor crowd pleaser.</p>
        </div>

        <!-- Recipe 5 -->
        <div class="recipe-card">
          <h3>5. Skillet Campfire Sweet Jalapeño Cornbread</h3>
          <div class="recipe-meta">
            <span><strong>Prep:</strong> 10 Mins</span>
            <span><strong>Bake Time:</strong> 30 Mins</span>
            <span><strong>Cook Temp:</strong> 375°F (Grill or Stovetop)</span>
            <span><strong>Yield:</strong> 8–10 Slices</span>
          </div>
          <p>
            An Appalachian classic baked in a sizzling cast-iron skillet, featuring crispy golden edges and a sweet, peppery crumb.
          </p>
          <p><strong>Key Ingredients:</strong> 2 cups self-rising cornmeal mix, 1 cup buttermilk, 2 eggs, 1/3 cup melted bacon grease or butter, 1/3 cup honey, 1 cup sharp cheddar cheese, and 1 diced jalapeño.</p>
          <p><strong>Method:</strong> Heat a 10-inch seasoned cast iron skillet on your grill with 2 tbsp bacon grease until smoking hot. Whisk batter ingredients, pour into the hot skillet, close grill lid, and bake indirectly at 375°F for 28 to 32 minutes until a knife comes out clean. Brush warm honey butter over the crust before slicing.</p>
        </div>
      </section>
"""

sec4_gear = """
      <!-- Section 4: Essential Tailgate Gear Checklist -->
      <section style="margin-top: 2.5rem;">
        <h2>🎒 Essential Tailgate Gear Checklist: From Campfire to Trackside</h2>
        <p>
          A seamless race weekend depends on smart packing. Keep your gear organized into these four primary camp stations:
        </p>

        <div class="gear-grid">
          <div class="gear-card">
            <h4>🧊 Coolers &amp; Storage</h4>
            <ul>
              <li><strong>Meat Cooler:</strong> Roto-molded cooler packed with block ice solely for perishable meats.</li>
              <li><strong>Drink Cooler:</strong> Dedicated cooler for canned beer, soda, and water with cubed ice.</li>
              <li><strong>Resting Cooler:</strong> Insulated cooler lined with clean towels for holding barbecue warm.</li>
              <li><strong>Heavy Foil &amp; Tongs:</strong> 18-inch heavy-duty foil rolls and long metal tongs for hot grates.</li>
            </ul>
          </div>

          <div class="gear-card">
            <h4>⛺ Shelter &amp; Seating</h4>
            <ul>
              <li><strong>Pop-Up Canopy (10x10):</strong> Heavy-gauge frame with UV fabric for midday shade.</li>
              <li><strong>Leg Weights / Stakes:</strong> Secure canopy legs against sudden mountain ridge gusts.</li>
              <li><strong>Folding Lawn Chairs:</strong> Heavy-duty camp chairs with built-in cup holders and mesh.</li>
              <li><strong>Outdoor Ground Mat:</strong> Keeps grass, damp soil, and gravel outside your camper entryway.</li>
            </ul>
          </div>

          <div class="gear-card">
            <h4>🏈 Games &amp; Tailgate Fun</h4>
            <ul>
              <li><strong>Cornhole Boards:</strong> Regulation wood boards and all-weather bean bags for campsite tournaments.</li>
              <li><strong>Bluetooth Speaker:</strong> Rugged, long-battery speaker for classic rock and scanner feeds.</li>
              <li><strong>Tailgate TV &amp; Antenna:</strong> Screen for streaming NASCAR practice, qualifying, and prerace shows.</li>
              <li><strong>String Lights &amp; Lanterns:</strong> LED illumination for cooking safely after sunset.</li>
            </ul>
          </div>

          <div class="gear-card">
            <h4>🧼 Prep Tools &amp; Sanitation</h4>
            <ul>
              <li><strong>Digital Meat Probe:</strong> Instant-read thermometer for pinpointing internal temperatures.</li>
              <li><strong>Insulated Food Gloves:</strong> Nitrile gloves with heat liners for pulling hot pork and brisket.</li>
              <li><strong>Hand Wash Station:</strong> Water jug with spigot, pump soap, and paper towels for clean prep.</li>
              <li><strong>Contractor Bags:</strong> Puncture-resistant trash bags to keep Sullivan County clean.</li>
            </ul>
          </div>
        </div>
      </section>
"""

sec5_timeline = """
      <!-- Section 5: Tailgate Timeline -->
      <section style="margin-top: 2.5rem;">
        <h2>⏰ Tailgate Timeline: Thursday Arrival Through Saturday Night Race</h2>
        <p>
          Pacing your cooking keeps race week enjoyable and avoids undercooked meat. Follow this master schedule from initial setup to the checkered flag:
        </p>

        <div class="timeline-block">
          <div class="timeline-badge">Thursday</div>
          <div class="timeline-body">
            <h4>Arrival, Campsite Setup &amp; Truck Series Racing</h4>
            <p>
              Arrive at the campground, level your RV, connect water, electric, and sewer hookups, and roll out your patio awning. Fire up the flat-top griddle for quick burgers or brats. Tune in to the UNOH 200 Truck Series race under the evening lights to kick off the weekend.
            </p>
          </div>
        </div>

        <div class="timeline-block">
          <div class="timeline-badge">Friday AM</div>
          <div class="timeline-body">
            <h4>Cast-Iron Breakfast &amp; Meat Rubbing</h4>
            <p>
              Cook bacon, eggs, and toast on the griddle. Trim the excess fat from your pork butts and briskets, apply your signature barbecue rubs, and store them cool so seasonings penetrate deep into the meat.
            </p>
          </div>
        </div>

        <div class="timeline-block">
          <div class="timeline-badge">Friday PM</div>
          <div class="timeline-body">
            <h4>Campground Cookout &amp; Overnight Pit Lighting</h4>
            <p>
              Smoke a batch of crispy chicken wings for Friday evening happy hour. Watch the Xfinity Series Food City 300 race. Before turning in around 10:30 PM, light your smoker and put on the pork shoulder or brisket for an all-night low-temperature cook.
            </p>
          </div>
        </div>

        <div class="timeline-block">
          <div class="timeline-badge">Saturday 8 AM</div>
          <div class="timeline-body">
            <h4>Race Day Temperature Check &amp; Rib Cook</h4>
            <p>
              Check your meat internal temperatures. Once pork or brisket reaches 165°F, wrap tightly in butcher paper or foil with butter. Put your St. Louis ribs onto the smoker to begin their 3-2-1 cook.
            </p>
          </div>
        </div>

        <div class="timeline-block">
          <div class="timeline-badge">Saturday 2 PM</div>
          <div class="timeline-body">
            <h4>Cooler Resting &amp; Cornbread Baking</h4>
            <p>
              Pull the tender pork butt and brisket off the smoker. Place wrapped meats into an insulated cooler lined with towels to rest. Glaze the ribs and bake the skillet jalapeño cornbread on the grill.
            </p>
          </div>
        </div>

        <div class="timeline-block">
          <div class="timeline-badge">Saturday 4 PM</div>
          <div class="timeline-body">
            <h4>Pre-Race Feast &amp; 15-Minute Track Walk</h4>
            <p>
              Shred the pulled pork, slice brisket, and feast with friends and campground neighbors. Pack your clear bags and track-approved soft coolers, then take the short 15-minute downhill walk to BMS for driver introductions.
            </p>
          </div>
        </div>

        <div class="timeline-block">
          <div class="timeline-badge">Saturday Night</div>
          <div class="timeline-body">
            <h4>Post-Race Campfire Celebration</h4>
            <p>
              Stroll casually back up to camp while 100,000 fans sit trapped in three hours of highway traffic. Stoke the campfire, toast s'mores, and reheat brisket sliders while rehashing every bump-and-run lap under the stars.
            </p>
          </div>
        </div>
      </section>
"""

mention2 = """
      <!-- Mention 2 with Phone CTA -->
      <div class="cta-inline">
        <p><strong>Secure your basecamp at Bristol Hilltop Camping for prime track views and zero post-race traffic</strong>—call <a href="tel:+14233835373" style="color: var(--color-accent-light); font-weight: 700;">(423) 383-5373</a> to reserve your site.</p>
      </div>
"""

sec6_hilltop = """
      <!-- Section 6: The Bristol Hilltop Tailgate Advantage -->
      <section style="margin-top: 2.5rem;">
        <h2>🏔️ The Bristol Hilltop Tailgate Advantage: Hilltop Views &amp; Big Setups</h2>
        <p>
          Where you park your RV or pitch your tent completely shapes your NASCAR experience. Many track-adjacent parking pastures cram vehicles bumper-to-bumper without electricity or green space. In contrast, <a href="../index.html"><strong>Bristol Hilltop Camping</strong></a> offers an elevated outdoor retreat:
        </p>
        <ul>
          <li><strong>Panoramic Hilltop Elevation:</strong> Situated high on a ridge at 133 Hilltop Street, our campground offers sweeping views of Sullivan County and sightlines toward the colossal BMS stadium structure. Cool evening mountain breezes sweep through camp, providing natural airflow for smokers.</li>
          <li><strong>Generous Lot Spacing:</strong> Real tailgating requires elbow room. Our spacious RV and tent sites offer plenty of room to extend full awnings, set up 10x10 canopies, arrange circle seating, and toss bean bags on a regulation cornhole court without crowding your neighbor.</li>
          <li><strong>Full Hookup Convenience:</strong> Enjoy municipal fresh water, sewer connections, and reliable 30-amp and 50-amp electrical service to power pellet grills, refrigerators, blenders, and outdoor TVs.</li>
          <li><strong>Easy 0.9-Mile Walk to BMS:</strong> Located only 0.9 miles from the speedway main gate, campers enjoy an easy 15-minute walk. You skip steep parking fees, avoid packed shuttle buses, and bypass the notorious 2-to-3-hour highway gridlock on US-11E and TN-394 after the race.</li>
        </ul>
      </section>
"""

sec7_bms_policy = """
      <!-- Section 7: Race Day Food Policies at BMS -->
      <section style="margin-top: 2.5rem;">
        <h2>🏟️ Race Day Food Policies at BMS: What You Can &amp; Can't Bring Inside</h2>
        <p>
          NASCAR is uniquely fan-friendly, allowing spectators to carry their own food and beverages inside the grandstands. However, Bristol Motor Speedway strictly enforces security rules at entry gates:
        </p>

        <div style="overflow-x: auto; margin: 1.25rem 0;">
          <table style="width: 100%; border-collapse: collapse; text-align: left; font-size: 0.93rem; border: 1px solid var(--color-border); border-radius: 8px; background: #ffffff;">
            <thead>
              <tr style="background: var(--color-primary-dark); color: #ffffff;">
                <th style="padding: 0.75rem 1rem;">Item</th>
                <th style="padding: 0.75rem 1rem;">✅ Allowed in BMS</th>
                <th style="padding: 0.75rem 1rem;">❌ Prohibited at Gates</th>
              </tr>
            </thead>
            <tbody>
              <tr style="border-bottom: 1px solid var(--color-border);">
                <td style="padding: 0.75rem 1rem; font-weight: 700;">Coolers</td>
                <td style="padding: 0.75rem 1rem;">One <strong>soft-sided cooler</strong> (max 14"x14"x14") with ice or freezer packs.</td>
                <td style="padding: 0.75rem 1rem; color: #b91c1c;">Hard-sided plastic, styrofoam, or wheeled coolers.</td>
              </tr>
              <tr style="border-bottom: 1px solid var(--color-border); background: #f9fafb;">
                <td style="padding: 0.75rem 1rem; font-weight: 700;">Bags</td>
                <td style="padding: 0.75rem 1rem;">One <strong>clear plastic tote</strong> (max 14"x14"x14") plus clutch purse (4.5"x6.5").</td>
                <td style="padding: 0.75rem 1rem; color: #b91c1c;">Opaque backpacks, duffle bags, tinted totes.</td>
              </tr>
              <tr style="border-bottom: 1px solid var(--color-border);">
                <td style="padding: 0.75rem 1rem; font-weight: 700;">Beverages</td>
                <td style="padding: 0.75rem 1rem;">Factory-sealed water, soda cans, energy drinks, and <strong>canned beer</strong>.</td>
                <td style="padding: 0.75rem 1rem; color: #b91c1c;">Glass bottles of any kind, hard liquor, open cups.</td>
              </tr>
              <tr style="background: #f9fafb;">
                <td style="padding: 0.75rem 1rem; font-weight: 700;">Food</td>
                <td style="padding: 0.75rem 1rem;">Foil-wrapped pulled pork sandwiches, brisket sliders, snacks, chips, cookies.</td>
                <td style="padding: 0.75rem 1rem; color: #b91c1c;">Open cooking elements, loose unbagged messy stews.</td>
              </tr>
            </tbody>
          </table>
        </div>

        <div class="callout-box callout-box--accent">
          <h3>💡 Pro Pitmaster Cooler Tip</h3>
          <p style="margin-bottom: 0;">
            Freeze four 16-oz water bottles solid before race day and line the bottom of your 14x14 soft cooler instead of using loose bagged ice. They keep your canned beverages and foil-wrapped barbecue sandwiches ice-cold without melting into a soggy mess, and you get crisp mountain drinking water as they thaw during Stage 2 and Stage 3.
          </p>
        </div>
      </section>
"""

sec8_local_bbq = """
      <!-- Section 8: Best Local Bristol BBQ Spots -->
      <section style="margin-top: 2.5rem;">
        <h2>🍽️ Best Local Bristol BBQ Spots If You Don't Want to Cook</h2>
        <p>
          Even passionate grillmasters occasionally want to hang up their tongs and let legendary local pitmasters handle dinner. Northeast Tennessee features a distinctive wood-fired barbecue tradition celebrated across the country:
        </p>

        <div style="display: grid; gap: 1.15rem; margin: 1.25rem 0;">
          <div style="background: var(--color-bg-alt); border: 1px solid var(--color-border); border-radius: var(--border-radius); padding: 1.15rem;">
            <h3 style="color: var(--color-primary); margin-top: 0; margin-bottom: 0.25rem; font-size: 1.15rem;">🍖 Ridgewood Barbecue (Bluff City, TN)</h3>
            <p style="font-size: 0.88rem; color: var(--color-text-light); margin-bottom: 0.4rem;">📍 900 Elizabethton Hwy, Bluff City, TN &bull; 15 Mins South of Track</p>
            <p style="margin-bottom: 0;">
              Founded in 1948, Ridgewood Barbecue is an iconic Appalachian institution. Their hallmark dish is hickory-smoked country ham and pork sliced paper-thin, flash-grilled, and smothered in their signature thick, sweet-tangy sauce. Served alongside blue cheese dip and fresh-cut French fries, it is a culinary pilgrimage for race fans. Call ahead for race weekend takeout orders!
            </p>
          </div>

          <div style="background: var(--color-bg-alt); border: 1px solid var(--color-border); border-radius: var(--border-radius); padding: 1.15rem;">
            <h3 style="color: var(--color-primary); margin-top: 0; margin-bottom: 0.25rem; font-size: 1.15rem;">🎸 Delta Blues BBQ (Bristol, TN)</h3>
            <p style="font-size: 0.88rem; color: var(--color-text-light); margin-bottom: 0.4rem;">📍 724 State Street, Bristol, TN &bull; Historic Downtown</p>
            <p style="margin-bottom: 0;">
              Located right on iconic State Street in downtown Bristol, Delta Blues dishes up slow-smoked Texas brisket, baby back ribs, pulled pork nachos, and an extensive craft beer list, often accompanied by live roots music.
            </p>
          </div>

          <div style="background: var(--color-bg-alt); border: 1px solid var(--color-border); border-radius: var(--border-radius); padding: 1.15rem;">
            <h3 style="color: var(--color-primary); margin-top: 0; margin-bottom: 0.25rem; font-size: 1.15rem;">🔥 Phil's Dream Pit (Kingsport / Bristol Corridor)</h3>
            <p style="font-size: 0.88rem; color: var(--color-text-light); margin-bottom: 0.4rem;">📍 4141 Fort Henry Dr, Kingsport, TN &bull; ~20 Mins Northwest</p>
            <p style="margin-bottom: 0;">
              A beloved open-pit barbecue joint cooking over hardwood logs. Phil's delivers fork-tender ribs, Carolina pulled pork, and tangy vinegar slaw. Picking up family packs on your drive in makes stocking your RV fridge effortless.
            </p>
          </div>
        </div>
      </section>
"""

mention3 = """
      <!-- Mention 3 with Phone CTA -->
      <div class="cta-inline">
        <p><strong>Whether you fire up your own smoker or bring back famous local barbecue</strong>, Bristol Hilltop Camping provides the ultimate race weekend home base. Call <a href="tel:+14233835373" style="color: var(--color-accent-light); font-weight: 700;">(423) 383-5373</a> to check weekend availability.</p>
      </div>
"""

sec9_community = """
      <!-- Section 9: Community Cookouts -->
      <section style="margin-top: 2.5rem;">
        <h2>🤝 Community Cookouts: Meeting Fellow Race Fans at the Campground</h2>
        <p>
          Great barbecue is meant to be shared. At Bristol Hilltop Camping, tailgating is a shared communal tradition that connects fans from all across North America. Multi-generational camping crews return every season, forging friendships that last decades.
        </p>
        <p>
          Campground potlucks develop naturally across our scenic ridge. On Friday and Saturday afternoons, you'll see neighbors aligning camp tables to create a sprawling Appalachian smorgasbord: one camper shares smoked chicken wings, another offers cast-iron cobbler, while others bring pimento cheese dip and baked beans.
        </p>
        <div class="callout-box">
          <h3>🤝 Good Neighbor Tailgate Etiquette</h3>
          <ul>
            <li><strong>Share Pit Wisdom:</strong> Swap dry rub recipes, compare smoker wood choices, and discuss team pit strategies.</li>
            <li><strong>Respect Midnight Quiet Hours:</strong> Tailgate hard during the day, but lower music volumes after midnight so everyone is rested for race day.</li>
            <li><strong>Keep Appalachian Wildlife Safe:</strong> Store food securely, wipe down grills, and seal grease traps to prevent nighttime critter visits.</li>
            <li><strong>Leave Your Lot Clean:</strong> Bag your trash and utilize campsite waste cans so our hilltop remains pristine for all visitors.</li>
          </ul>
        </div>
      </section>
"""

sec10_faq = """
      <!-- Section 10: FAQ Section -->
      <section style="margin-top: 3rem;" id="faq">
        <h2>❓ Frequently Asked Questions: Race Weekend BBQ &amp; Tailgating</h2>
        <p>
          Here are answers to the six most common questions campers have about race weekend tailgating and campfire barbecue:
        </p>

        <div class="faq__list" style="margin-top: 1.5rem;">

          <div class="faq__item">
            <button class="faq__question" aria-expanded="false">
              <span>Can I bring my own charcoal grill or smoker to Bristol Hilltop Camping?</span>
              <span class="faq__icon">+</span>
            </button>
            <div class="faq__answer">
              <p>
                Yes! Bristol Hilltop Camping welcomes smokers, charcoal grills, pellet cookers, and propane flat-tops. Grills must be placed on stable, level ground away from camper awnings and dry grass. Ash and embers must be fully cooled and placed in designated metal disposal cans.
              </p>
            </div>
          </div>

          <div class="faq__item">
            <button class="faq__question" aria-expanded="false">
              <span>What food and drinks can I bring inside Bristol Motor Speedway on race day?</span>
              <span class="faq__icon">+</span>
            </button>
            <div class="faq__answer">
              <p>
                Each ticket holder can carry one soft-sided cooler (up to 14x14x14 inches) and one clear bag (up to 14x14x14 inches). Fans may pack ice packs, canned beer, soda, water, and homemade food like sandwiches or barbecue. Glass containers, hard liquor, and hard-sided coolers are strictly prohibited.
              </p>
            </div>
          </div>

          <div class="faq__item">
            <button class="faq__question" aria-expanded="false">
              <span>When should I put large meats on the smoker for a Saturday night race?</span>
              <span class="faq__icon">+</span>
            </button>
            <div class="faq__answer">
              <p>
                For whole briskets or large pork butts needing 10 to 14 hours of smoke, start your pit Friday night around 10:00 PM or early Saturday morning at 4:00 AM. This timing lets the meat finish by early afternoon, leaving 2 hours to rest in an insulated cooler before slicing for a 4:00 PM feast.
              </p>
            </div>
          </div>

          <div class="faq__item">
            <button class="faq__question" aria-expanded="false">
              <span>What is the best method to keep food cold across a four-day race weekend?</span>
              <span class="faq__icon">+</span>
            </button>
            <div class="faq__answer">
              <p>
                Follow the two-cooler method: dedicate one premium roto-molded cooler strictly for raw meats and perishables, and use a second cooler for beverages. Place block ice on the bottom overlaid with cubed ice, keep coolers shaded under your awning, and minimize lid openings.
              </p>
            </div>
          </div>

          <div class="faq__item">
            <button class="faq__question" aria-expanded="false">
              <span>How do campers organize community cookouts at Bristol Hilltop Camping?</span>
              <span class="faq__icon">+</span>
            </button>
            <div class="faq__answer">
              <p>
                Campground cookouts come together naturally! Campers set up folding tables along campsite lanes on Friday and Saturday afternoons, sharing extra ribs, smoked wings, and homemade sauces while swapping race picks with neighbors before walking down to the track.
              </p>
            </div>
          </div>

          <div class="faq__item">
            <button class="faq__question" aria-expanded="false">
              <span>Why is camping at Bristol Hilltop better for tailgating than day parking at BMS?</span>
              <span class="faq__icon">+</span>
            </button>
            <div class="faq__answer">
              <p>
                Day parking lots at Bristol Motor Speedway cost up to $50 daily, lack electricity and water hookups, have tight spacing, and suffer from 2- to 3-hour post-race traffic gridlocks. Camping at Bristol Hilltop gives you spacious lots, full hookups for pellet grills and TVs, scenic hilltop views, and a simple 15-minute walk that bypasses traffic entirely.
              </p>
            </div>
          </div>

        </div>
      </section>
"""

sec11_conclusion = """
      <!-- Section 11: Final Summary & Mention 4 -->
      <section style="margin-top: 3.25rem; border-top: 1px solid var(--color-border); padding-top: 2rem;">
        <h2>🏁 Claim Your Spot on the Hill for the Next Bristol Race Weekend</h2>
        <p>
          From wood smoke curling above the trees and mouth-watering pulled pork sliders to cold beverages shared with newfound friends as engines roar in Thunder Valley, a <strong>Bristol Motor Speedway tailgate</strong> is the pinnacle of American motorsport culture. Skip cramped, overpriced hotel rooms and avoid hours trapped in highway gridlock.
        </p>
        <p>
          Camp on our scenic ridge, set up your smoker, and experience NASCAR weekend the way it was always intended. <strong>Ready to join the best tailgate party in NASCAR?</strong> Book your campsite at Bristol Hilltop Camping by calling <a href="tel:+14233835373"><strong>(423) 383-5373</strong></a> today!
        </p>
      </section>
"""

body = intro + sec1_culture + sec2_setup + mention1 + sec3_recipes + sec4_gear + sec5_timeline + mention2 + sec6_hilltop + sec7_bms_policy + sec8_local_bbq + mention3 + sec9_community + sec10_faq + sec11_conclusion

clean = re.sub(r'<[^>]+>', ' ', body)
words = clean.split()
print("Current body word count:", len(words))
