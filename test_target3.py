import re

intro = """
      <!-- Introduction -->
      <section>
        <p style="font-size: 1.15rem; line-height: 1.75; color: var(--color-text);">
          When twilight blankets the Appalachian ridges of Sullivan County and floodlights ignite over <strong>"The Last Great Colosseum,"</strong> a mouth-watering aroma drifts across the hills. It is the perfume of hickory smoke, sizzling pork fat, and tangy mop sauce. At Bristol Motor Speedway, the fierce racing on the 0.533-mile concrete oval is matched only by the legendary cookouts across the campgrounds.
        </p>
        <p>
          Whether you are a seasoned pitmaster hauling an offset smoker or an RV camper with a portable flat-top griddle, an authentic <strong>Bristol Motor Speedway tailgate</strong> is an essential NASCAR ritual. This comprehensive <strong>NASCAR tailgate guide</strong> provides everything you need for the ultimate <strong>race weekend BBQ camping Bristol</strong> experience—from grill selection and five pit recipes to gear checklists, track cooler rules, and the unmatched energy of a <strong>Bristol race night party</strong>.
        </p>
      </section>
"""

sec1 = """
      <!-- Section 1: The Legendary Bristol Tailgate Culture -->
      <section style="margin-top: 2.5rem;">
        <h2>🏁 The Legendary Bristol Tailgate Culture: Why It's the Best in NASCAR</h2>
        <p>
          Tailgating happens across NASCAR, but Bristol's culture is celebrated as the best in motorsport. Thunder Valley sits carved into an Appalachian mountain bowl, amplifying cheers, revving engines, and hardwood smoke across the ridges.
        </p>
        <p>
          Fans celebrate from Thursday through Sunday. Rivalries are intense on the high banks, but mountain hospitality rules the campground:
        </p>
        <div class="quote-box">
          &ldquo;Walk down any row of campers at Bristol and you are family. Fans share cold drinks, trade barbecue samples, and invite you to pull up a lawn chair by the fire.&rdquo;
        </div>
        <p>
          Spring's <a href="../food-city-500.html"><strong>Food City 500</strong></a> brings sunny daytime cookouts under blooming dogwoods, while September's <a href="../bass-pro-night-race.html"><strong>Bass Pro Shops Night Race</strong></a> delivers an electric playoff festival where smokers run until sunrise.
        </p>
      </section>
"""

sec2 = """
      <!-- Section 2: BBQ Setup Guide -->
      <section style="margin-top: 2.5rem;">
        <h2>🔥 BBQ Setup Guide: What Grill to Bring to Your Campsite</h2>
        <p>
          Choosing the right cooker for campground life ensures great barbecue without hassle:
        </p>

        <div class="gear-grid">
          <div class="gear-card">
            <h4>🍖 Pellet Smokers (Traeger, Green Mountain)</h4>
            <p><strong>Best For:</strong> Set-and-forget cooking while exploring the track.</p>
            <ul>
              <li>Holds steady 225°F for 12 hours with hardwood smoke.</li>
              <li>Requires 110V power; full hookup RV sites make this effortless.</li>
              <li>Keep pellets in sealed waterproof buckets.</li>
            </ul>
          </div>

          <div class="gear-card">
            <h4>🪵 Charcoal Smokers (Weber, WSM)</h4>
            <p><strong>Best For:</strong> Deep smoke rings and authentic wood bark.</p>
            <ul>
              <li>Unbeatable wood-fired flavor without electricity.</li>
              <li>Requires damper management and ash clean-up.</li>
              <li>Bring a metal bucket with lid for hot coals.</li>
            </ul>
          </div>

          <div class="gear-card">
            <h4>🍳 Portable Propane Griddles (Blackstone 22")</h4>
            <p><strong>Best For:</strong> Fast breakfasts and quick pre-race meals.</p>
            <ul>
              <li>Instant heat, zero ash; perfect for smashburgers and bacon.</li>
              <li>Lacks wood smoke for low-and-slow cuts.</li>
              <li>Use a 20-lb propane tank adapter hose.</li>
            </ul>
          </div>
        </div>

        <div class="callout-box">
          <h3>⚠️ Grilling Safety &amp; Etiquette</h3>
          <p style="margin-bottom: 0;">
            Place cookers on level ground 10 feet from camper awnings. Ridge breezes carry sparks, so never leave coals unattended and keep an extinguisher or water bucket nearby.
          </p>
        </div>
      </section>
"""

m1 = """
      <!-- Mention 1 with Phone CTA -->
      <div class="cta-inline">
        <p><strong>Planning to smoke your own brisket or ribs on race weekend?</strong> Reserve a spacious full hookup RV site with 30/50-amp power at Bristol Hilltop Camping by calling <a href="tel:+14233835373" style="color: var(--color-accent-light); font-weight: 700;">(423) 383-5373</a>.</p>
      </div>
"""

sec3 = """
      <!-- Section 3: Top 5 Race Weekend BBQ Recipes -->
      <section style="margin-top: 2.5rem;">
        <h2>🏆 Top 5 Race Weekend BBQ Recipes for Bristol Campers</h2>
        <p>
          These five crowd-pleasing recipes are engineered for smooth campsite preparation:
        </p>

        <!-- Recipe 1 -->
        <div class="recipe-card">
          <h3>1. Colosseum Pulled Pork Butt (Hickory Smoked Pork)</h3>
          <div class="recipe-meta">
            <span><strong>Prep:</strong> 15 Mins</span>
            <span><strong>Smoke:</strong> 8–10 Hrs at 225°F</span>
            <span><strong>Yield:</strong> 12–15 Servings</span>
          </div>
          <p>
            Coat an 8-lb bone-in pork butt with mustard and sweet brown-sugar rub. Smoke over hickory at 225°F for 5 hours. Spritz with apple cider vinegar, wrap in heavy foil with butter and brown sugar, and cook at 250°F until tender at 203°F. Rest in a cooler for 2 hours before pulling onto brioche buns with slaw.
          </p>
        </div>

        <!-- Recipe 2 -->
        <div class="recipe-card">
          <h3>2. Thunder Valley Smoked St. Louis Ribs (3-2-1 Method)</h3>
          <div class="recipe-meta">
            <span><strong>Prep:</strong> 15 Mins</span>
            <span><strong>Smoke:</strong> 6 Hrs at 225°F</span>
            <span><strong>Yield:</strong> 4–6 Servings</span>
          </div>
          <p>
            Season 2 racks of ribs with pork rub. Smoke meat-side up at 225°F with applewood for 3 hours. Wrap tightly in foil with butter, brown sugar, and honey for 2 hours. Unwrap, brush with sweet barbecue sauce, and cook 1 final hour until the glaze caramelizes into a gleaming lacquer. Slice and serve hot.
          </p>
        </div>

        <!-- Recipe 3 -->
        <div class="recipe-card">
          <h3>3. Overnight Brisket Sliders with Pickled Jalapeño Slaw</h3>
          <div class="recipe-meta">
            <span><strong>Prep:</strong> 20 Mins</span>
            <span><strong>Smoke:</strong> 12–14 Hrs at 225°F</span>
            <span><strong>Yield:</strong> 16–20 Sliders</span>
          </div>
          <p>
            Season a trimmed brisket with coarse salt and pepper. Smoke overnight at 225°F over oak or hickory. Wrap in butcher paper at 165°F and cook until probe-tender (202°F). Rest 2 hours in a cooler, slice thin, and serve on sweet rolls with slaw and pickled jalapeños.
          </p>
        </div>

        <!-- Recipe 4 -->
        <div class="recipe-card">
          <h3>4. High-Banked Smoked &amp; Crisped Wings (Alabama White &amp; Buffalo)</h3>
          <div class="recipe-meta">
            <span><strong>Prep:</strong> 10 Mins</span>
            <span><strong>Cook:</strong> 1.5 Hrs at 250°F / 400°F</span>
            <span><strong>Yield:</strong> 6–8 Servings</span>
          </div>
          <p>
            Toss dried wings with baking powder and poultry rub. Smoke at 250°F for 45 minutes, then crisp at 400°F for 30 minutes until golden. Toss half in spicy Buffalo sauce and dunk the rest in tangy Alabama white barbecue sauce (mayo, cider vinegar, pepper, horseradish).
          </p>
        </div>

        <!-- Recipe 5 -->
        <div class="recipe-card">
          <h3>5. Skillet Campfire Sweet Jalapeño Cornbread</h3>
          <div class="recipe-meta">
            <span><strong>Prep:</strong> 10 Mins</span>
            <span><strong>Bake:</strong> 30 Mins at 375°F</span>
            <span><strong>Yield:</strong> 8–10 Slices</span>
          </div>
          <p>
            Preheat a 10-inch cast iron skillet with bacon grease on your grill. Whisk 2 cups cornmeal mix, buttermilk, eggs, melted butter, honey, cheddar cheese, and diced jalapeño. Pour into the skillet and bake indirectly at 375°F for 30 minutes. Brush with honey butter before slicing.
          </p>
        </div>
      </section>
"""

sec4 = """
      <!-- Section 4: Essential Tailgate Gear Checklist -->
      <section style="margin-top: 2.5rem;">
        <h2>🎒 Essential Tailgate Gear Checklist: From Campfire to Trackside</h2>
        <p>
          Organize your gear into four key camp stations to ensure a stress-free weekend:
        </p>

        <div class="gear-grid">
          <div class="gear-card">
            <h4>🧊 Coolers &amp; Storage</h4>
            <ul>
              <li><strong>Meat Cooler:</strong> Roto-molded cooler with block ice for raw meats.</li>
              <li><strong>Drink Cooler:</strong> Dedicated cooler for beers, soda, and water.</li>
              <li><strong>Resting Cooler:</strong> Insulated cooler to hold smoked barbecue warm.</li>
              <li><strong>Foil &amp; Tongs:</strong> Heavy 18-inch foil and long tongs for hot grates.</li>
            </ul>
          </div>

          <div class="gear-card">
            <h4>⛺ Shelter &amp; Seating</h4>
            <ul>
              <li><strong>Pop-Up Canopy:</strong> 10x10 frame with UV fabric for midday shade.</li>
              <li><strong>Leg Weights:</strong> Secure canopy legs against mountain gusts.</li>
              <li><strong>Camp Chairs:</strong> Folding chairs with built-in cup holders.</li>
              <li><strong>Ground Mat:</strong> Breathable mat keeps dirt outside your camper.</li>
            </ul>
          </div>

          <div class="gear-card">
            <h4>🏈 Games &amp; Fun</h4>
            <ul>
              <li><strong>Cornhole Boards:</strong> Regulation wood boards for tournaments.</li>
              <li><strong>Bluetooth Speaker:</strong> Rugged speaker for music and radio feeds.</li>
              <li><strong>Tailgate TV:</strong> Monitor for practice and qualifying broadcasts.</li>
              <li><strong>String Lights:</strong> LED campsite lighting for safe evening cooking.</li>
            </ul>
          </div>

          <div class="gear-card">
            <h4>🧼 Tools &amp; Clean-Up</h4>
            <ul>
              <li><strong>Digital Meat Probe:</strong> Instant thermometer for target temps.</li>
              <li><strong>Insulated Gloves:</strong> Heat-safe food gloves for pulling hot pork.</li>
              <li><strong>Wash Station:</strong> Water jug with spigot, soap, and paper towels.</li>
              <li><strong>Contractor Bags:</strong> Heavy trash bags to keep your lot spotless.</li>
            </ul>
          </div>
        </div>
      </section>
"""

sec5 = """
      <!-- Section 5: Tailgate Timeline -->
      <section style="margin-top: 2.5rem;">
        <h2>⏰ Tailgate Timeline: Thursday Arrival Through Saturday Night Race</h2>
        <p>
          Pacing your cooking keeps race week relaxed and ensures dinner is ready on schedule:
        </p>

        <div class="timeline-block">
          <div class="timeline-badge">Thursday</div>
          <div class="timeline-body">
            <h4>Arrival &amp; Basecamp Setup</h4>
            <p>
              Check in, level your camper, connect hookups, and roll out your awning. Grill burgers on the flat-top, then enjoy the Thursday night UNOH 200 Truck Series race.
            </p>
          </div>
        </div>

        <div class="timeline-block">
          <div class="timeline-badge">Friday AM</div>
          <div class="timeline-body">
            <h4>Camp Breakfast &amp; Meat Rubbing</h4>
            <p>
              Cook bacon and eggs on the griddle. Trim briskets and pork butts, apply rubs, and keep meats chilled so seasonings cure deep before smoking.
            </p>
          </div>
        </div>

        <div class="timeline-block">
          <div class="timeline-badge">Friday PM</div>
          <div class="timeline-body">
            <h4>Wings &amp; Overnight Pit Lighting</h4>
            <p>
              Smoke wings for happy hour and watch the Xfinity Series race. Before bed at 10:30 PM, light your smoker and put on pork or brisket for an overnight cook.
            </p>
          </div>
        </div>

        <div class="timeline-block">
          <div class="timeline-badge">Saturday 8 AM</div>
          <div class="timeline-body">
            <h4>Meat Wrap &amp; Rib Cook</h4>
            <p>
              Wrap brisket or pork in butcher paper once the bark sets (~165°F). Put St. Louis ribs onto the smoker to begin their 3-2-1 cook.
            </p>
          </div>
        </div>

        <div class="timeline-block">
          <div class="timeline-badge">Saturday 2 PM</div>
          <div class="timeline-body">
            <h4>Cooler Rest &amp; Cornbread Baking</h4>
            <p>
              Place probe-tender meats into a cooler to rest. Glaze ribs and bake skillet jalapeño cornbread on the grill.
            </p>
          </div>
        </div>

        <div class="timeline-block">
          <div class="timeline-badge">Saturday 4 PM</div>
          <div class="timeline-body">
            <h4>Pre-Race Feast &amp; Track Walk</h4>
            <p>
              Shred pork, slice brisket, and feast with friends. Pack track-approved soft coolers, then take the easy 15-minute downhill walk to BMS.
            </p>
          </div>
        </div>

        <div class="timeline-block">
          <div class="timeline-badge">Saturday Night</div>
          <div class="timeline-body">
            <h4>Post-Race Campfire Celebration</h4>
            <p>
              Stroll back to camp while highway traffic idles in gridlock. Stoke the campfire, toast s'mores, and rehash the race under the stars.
            </p>
          </div>
        </div>
      </section>
"""

m2 = """
      <!-- Mention 2 with Phone CTA -->
      <div class="cta-inline">
        <p><strong>Secure your basecamp at Bristol Hilltop Camping for prime track views and zero post-race traffic</strong>—call <a href="tel:+14233835373" style="color: var(--color-accent-light); font-weight: 700;">(423) 383-5373</a> to reserve your site.</p>
      </div>
"""

sec6 = """
      <!-- Section 6: The Bristol Hilltop Tailgate Advantage -->
      <section style="margin-top: 2.5rem;">
        <h2>🏔️ The Bristol Hilltop Tailgate Advantage: Hilltop Views &amp; Big Setups</h2>
        <p>
          Where you camp shapes your entire race experience. Unlike crowded gravel day-lots, <a href="../index.html"><strong>Bristol Hilltop Camping</strong></a> offers an elevated outdoor retreat:
        </p>
        <ul>
          <li><strong>Panoramic Hilltop Elevation:</strong> Perched on a ridge at 133 Hilltop Street, our grounds offer scenic mountain views and BMS stadium sightlines, with refreshing breezes that clear smoker exhaust.</li>
          <li><strong>Generous Lot Spacing:</strong> Ample room to extend full RV awnings, erect 10x10 canopies, arrange circle seating, and set up regulation cornhole courts without crowding neighbors.</li>
          <li><strong>Full Hookup Convenience:</strong> Municipal fresh water, sewer hookups, and reliable 30-amp and 50-amp power for pellet smokers, refrigerators, and outdoor TVs.</li>
          <li><strong>Easy 0.9-Mile Walk to BMS:</strong> Just 0.9 miles from the main gate, campers enjoy an easy 15-minute walk—avoiding parking fees and 2-to-3-hour post-race highway gridlocks.</li>
        </ul>
      </section>
"""

sec7 = """
      <!-- Section 7: Race Day Food Policies at BMS -->
      <section style="margin-top: 2.5rem;">
        <h2>🏟️ Race Day Food Policies at BMS: What You Can &amp; Can't Bring Inside</h2>
        <p>
          Bristol Motor Speedway allows fans to bring food and drinks into the grandstands, subject to gate security rules:
        </p>

        <div style="overflow-x: auto; margin: 1.25rem 0;">
          <table style="width: 100%; border-collapse: collapse; text-align: left; font-size: 0.92rem; border: 1px solid var(--color-border); border-radius: 8px; background: #ffffff;">
            <thead>
              <tr style="background: var(--color-primary-dark); color: #ffffff;">
                <th style="padding: 0.6rem 0.85rem;">Category</th>
                <th style="padding: 0.6rem 0.85rem;">✅ Permitted at BMS</th>
                <th style="padding: 0.6rem 0.85rem;">❌ Prohibited at Gates</th>
              </tr>
            </thead>
            <tbody>
              <tr style="border-bottom: 1px solid var(--color-border);">
                <td style="padding: 0.6rem 0.85rem; font-weight: 700;">Coolers</td>
                <td style="padding: 0.6rem 0.85rem;">One <strong>soft-sided cooler</strong> (max 14"x14"x14") with ice packs.</td>
                <td style="padding: 0.6rem 0.85rem; color: #b91c1c;">Hard plastic, styrofoam, or rolling coolers.</td>
              </tr>
              <tr style="border-bottom: 1px solid var(--color-border); background: #f9fafb;">
                <td style="padding: 0.6rem 0.85rem; font-weight: 700;">Bags</td>
                <td style="padding: 0.6rem 0.85rem;">One <strong>clear plastic tote</strong> (max 14"x14"x14") plus clutch (4.5"x6.5").</td>
                <td style="padding: 0.6rem 0.85rem; color: #b91c1c;">Opaque backpacks, duffle bags, dark totes.</td>
              </tr>
              <tr style="border-bottom: 1px solid var(--color-border);">
                <td style="padding: 0.6rem 0.85rem; font-weight: 700;">Beverages</td>
                <td style="padding: 0.6rem 0.85rem;">Sealed water, soda cans, energy drinks, and <strong>canned beer</strong>.</td>
                <td style="padding: 0.6rem 0.85rem; color: #b91c1c;">Glass bottles, hard liquor, open containers.</td>
              </tr>
              <tr style="background: #f9fafb;">
                <td style="padding: 0.6rem 0.85rem; font-weight: 700;">Food</td>
                <td style="padding: 0.6rem 0.85rem;">Foil-wrapped sandwiches, brisket sliders, snacks, chips.</td>
                <td style="padding: 0.6rem 0.85rem; color: #b91c1c;">Open cooking elements, loose unbagged stews.</td>
              </tr>
            </tbody>
          </table>
        </div>

        <div class="callout-box callout-box--accent">
          <h3>💡 Pro Pitmaster Cooler Tip</h3>
          <p style="margin-bottom: 0;">
            Freeze four water bottles solid before race day to line the bottom of your soft cooler. They keep food and beer cold without soggy waterlogging and provide ice-cold drinking water as they thaw.
          </p>
        </div>
      </section>
"""

sec8 = """
      <!-- Section 8: Best Local Bristol BBQ Spots -->
      <section style="margin-top: 2.5rem;">
        <h2>🍽️ Best Local Bristol BBQ Spots If You Don't Want to Cook</h2>
        <p>
          Need a break from cooking? Northeast Tennessee boasts renowned smokehouses for race weekend takeout:
        </p>

        <div style="display: grid; gap: 1rem; margin: 1.25rem 0;">
          <div style="background: var(--color-bg-alt); border: 1px solid var(--color-border); border-radius: var(--border-radius); padding: 1rem;">
            <h3 style="color: var(--color-primary); margin-top: 0; margin-bottom: 0.2rem; font-size: 1.05rem;">🍖 Ridgewood Barbecue (Bluff City, TN)</h3>
            <p style="font-size: 0.85rem; color: var(--color-text-light); margin-bottom: 0.3rem;">📍 900 Elizabethton Hwy, Bluff City &bull; 15 Mins South of Track</p>
            <p style="margin-bottom: 0;">
              Founded in 1948, Ridgewood is an iconic Appalachian barbecue institution. Famous for hickory-smoked pork sliced paper-thin, flash-grilled, and smothered in sweet-tangy sauce. Served with blue cheese dip and fresh-cut fries, it is a must-visit for race fans.
            </p>
          </div>

          <div style="background: var(--color-bg-alt); border: 1px solid var(--color-border); border-radius: var(--border-radius); padding: 1rem;">
            <h3 style="color: var(--color-primary); margin-top: 0; margin-bottom: 0.2rem; font-size: 1.05rem;">🎸 Delta Blues BBQ (Bristol, TN)</h3>
            <p style="font-size: 0.85rem; color: var(--color-text-light); margin-bottom: 0.3rem;">📍 724 State Street, Bristol &bull; Historic Downtown</p>
            <p style="margin-bottom: 0;">
              Located on historic State Street, Delta Blues serves slow-smoked Texas brisket, baby back ribs, pulled pork nachos, and local craft beers with live bluegrass and roots music.
            </p>
          </div>

          <div style="background: var(--color-bg-alt); border: 1px solid var(--color-border); border-radius: var(--border-radius); padding: 1rem;">
            <h3 style="color: var(--color-primary); margin-top: 0; margin-bottom: 0.2rem; font-size: 1.05rem;">🔥 Phil's Dream Pit (Kingsport / Bristol Corridor)</h3>
            <p style="font-size: 0.85rem; color: var(--color-text-light); margin-bottom: 0.3rem;">📍 4141 Fort Henry Dr, Kingsport &bull; ~20 Mins Northwest</p>
            <p style="margin-bottom: 0;">
              An authentic wood-fired pit smoking over local hardwoods. Phil's delivers fork-tender ribs, pulled pork, and vinegar slaw. Grabbing family packs makes campsite meal planning easy.
            </p>
          </div>
        </div>
      </section>
"""

m3 = """
      <!-- Mention 3 with Phone CTA -->
      <div class="cta-inline">
        <p><strong>Whether you fire up your own smoker or bring back famous local barbecue</strong>, Bristol Hilltop Camping provides the ultimate race weekend home base. Call <a href="tel:+14233835373" style="color: var(--color-accent-light); font-weight: 700;">(423) 383-5373</a> to check weekend availability.</p>
      </div>
"""

sec9 = """
      <!-- Section 9: Community Cookouts -->
      <section style="margin-top: 2.5rem;">
        <h2>🤝 Community Cookouts: Meeting Fellow Race Fans at the Campground</h2>
        <p>
          Great barbecue is meant to be shared. At Bristol Hilltop Camping, tailgating connects fans from across North America. Multi-generational camping groups return each year, creating lasting friendships.
        </p>
        <p>
          Campground potlucks develop naturally across our ridge. On Friday and Saturday afternoons, neighbors align camp tables into an Appalachian feast: campers share smoked wings, cobbler, pimento cheese dip, and beans.
        </p>
        <div class="callout-box">
          <h3>🤝 Good Neighbor Tailgate Etiquette</h3>
          <ul>
            <li><strong>Share Pit Wisdom:</strong> Swap rub recipes, wood tips, and race strategies.</li>
            <li><strong>Respect Quiet Hours:</strong> Tailgate hard by day, but lower music volume after midnight so campers can sleep.</li>
            <li><strong>Wildlife Safety:</strong> Store food securely and clean grease trays to avoid attracting mountain critters.</li>
            <li><strong>Keep Lots Clean:</strong> Bag trash and use camp bins to keep our hilltop ridge spotless.</li>
          </ul>
        </div>
      </section>
"""

sec10 = """
      <!-- Section 10: FAQ Section -->
      <section style="margin-top: 3rem;" id="faq">
        <h2>❓ Frequently Asked Questions: Race Weekend BBQ &amp; Tailgating</h2>
        <p>
          Here are answers to the six most common questions campers ask about race weekend tailgating:
        </p>

        <div class="faq__list" style="margin-top: 1.5rem;">

          <div class="faq__item">
            <button class="faq__question" aria-expanded="false">
              <span>Can I bring my own charcoal grill or smoker to Bristol Hilltop Camping?</span>
              <span class="faq__icon">+</span>
            </button>
            <div class="faq__answer">
              <p>
                Yes! Bristol Hilltop Camping welcomes smokers, charcoal kettles, pellet cookers, and propane flat-tops. Grills must sit on stable ground away from awnings and dry grass. Cool all embers before disposing in designated metal cans.
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
                Each ticketed fan can carry one soft-sided cooler (up to 14x14x14 inches) and one clear bag (up to 14x14x14 inches). Pack ice packs, canned beer, soda, water, and homemade food like barbecue sandwiches. Glass, liquor, and hard coolers are prohibited.
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
                For briskets or pork butts needing 10 to 14 hours of cook time, start smoking Friday night at 10:00 PM or Saturday morning at 4:00 AM. This lets meats finish by 1:00 PM, allowing 2 hours to rest before a 4:00 PM pre-race feast.
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
                Use the two-cooler method: reserve one roto-molded cooler strictly for raw meat with block ice, and use a second cooler for drinks. Keep coolers shaded under your awning and limit lid openings.
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
                Cookouts happen organically! Campers set up tables in campsite lanes on Friday and Saturday afternoons, sharing extra ribs, smoked wings, and sides with neighbors before walking to the track together.
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
                Speedway day-lots cost up to $50, lack electric hookups, and trap fans in 2-to-3-hour exit gridlocks. Bristol Hilltop provides spacious lots, full hookups for pellet grills and TVs, hilltop views, and a simple 15-minute walk that bypasses traffic entirely.
              </p>
            </div>
          </div>

        </div>
      </section>
"""

sec11 = """
      <!-- Section 11: Final Summary & Mention 4 -->
      <section style="margin-top: 3.25rem; border-top: 1px solid var(--color-border); padding-top: 2rem;">
        <h2>🏁 Claim Your Spot on the Hill for the Next Bristol Race Weekend</h2>
        <p>
          From wood smoke curling above the trees to cold drinks shared with friends as engines roar in Thunder Valley, a <strong>Bristol Motor Speedway tailgate</strong> is the pinnacle of NASCAR culture. Skip cramped hotel rooms and avoid hours trapped in highway gridlock.
        </p>
        <p>
          Camp on our scenic ridge, fire up your smoker, and experience race weekend the right way. <strong>Ready to join the best tailgate party in NASCAR?</strong> Book your campsite at Bristol Hilltop Camping by calling <a href="tel:+14233835373"><strong>(423) 383-5373</strong></a> today!
        </p>
      </section>
"""

full_article = intro + sec1 + sec2 + m1 + sec3 + sec4 + sec5 + m2 + sec6 + sec7 + sec8 + m3 + sec9 + sec10 + sec11
words = re.sub(r'<[^>]+>', ' ', full_article).split()
print("Total words in calibrated article 3:", len(words))
