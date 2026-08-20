const fs = require("fs");
const {
  Document, Packer, Paragraph, TextRun, HeadingLevel, ImageRun,
  Table, TableRow, TableCell, WidthType, ShadingType,
  AlignmentType, PageBreak
} = require("docx");

const TEAL = "1F9E92";
const MUTED = "5C6B7C";

function img(path, width, height) {
  const data = fs.readFileSync(path);
  return new ImageRun({ type: "png", data, transformation: { width, height } });
}
function h1(text) {
  return new Paragraph({ heading: HeadingLevel.HEADING_1, spacing: { before: 300, after: 160 }, children: [new TextRun({ text, bold: true })] });
}
function p(text, opts = {}) {
  return new Paragraph({ spacing: { after: 160 }, children: [new TextRun({ text, ...opts })] });
}
function bullet(text) {
  return new Paragraph({ text, bullet: { level: 0 }, spacing: { after: 80 } });
}
function actionRow(step, action, owner, timeframe, header = false) {
  const cell = (text, width) => new TableCell({
    width: { size: width, type: WidthType.DXA },
    shading: header ? { type: ShadingType.CLEAR, fill: "121922" } : undefined,
    children: [new Paragraph({ children: [new TextRun({ text, bold: header, color: header ? "FFFFFF" : "000000", size: 20 })] })],
  });
  return new TableRow({ children: [cell(step, 1200), cell(action, 4800), cell(owner, 1800), cell(timeframe, 1800)] });
}

const doc = new Document({
  sections: [{
    properties: { page: { size: { width: 12240, height: 15840 } } },
    children: [
      new Paragraph({ spacing: { after: 60 }, children: [new TextRun({ text: "ELEVATETECH", bold: true, color: TEAL, size: 22 })] }),
      new Paragraph({ spacing: { after: 260 }, children: [new TextRun({ text: "Performance & Competitive Analysis", size: 44, bold: true })] }),
      new Paragraph({ spacing: { after: 40 }, children: [new TextRun({ text: "Prepared for: SocialSprout — Instagram Marketing Agency, Bangalore (sample / illustrative client)", italics: true, color: MUTED })] }),
      new Paragraph({ spacing: { after: 400 }, children: [new TextRun({ text: "Period: September 2025 – August 2026", italics: true, color: MUTED })] }),

      p("This report is a sample project built by ElevateTech to demonstrate our data analysis and business reporting process. SocialSprout is a fictional agency, and all figures below are synthetic data constructed to be realistic — not real financial records.", { italics: true, color: MUTED, size: 20 }),

      h1("Executive Summary"),
      p("Over the past twelve months, SocialSprout grew monthly revenue from roughly ₹4.45L to ₹8.07L, alongside active client count more than doubling from 14 to 29. Despite this growth, SocialSprout holds an estimated 28% share of the three-agency Bangalore market being tracked, well behind ViralNest Media at 54%, and ahead of Boostly Creators at 17%."),
      p("The standout finding: SocialSprout converts client-acquisition spend into revenue almost twice as efficiently as ViralNest Media (₹12.89 vs ₹6.91 per rupee spent). ViralNest's larger revenue is being bought with a acquisition budget roughly 3.5x the size of SocialSprout's — not won through better conversion. That gap is the clearest lever available."),

      h1("Current Performance"),
      p("Revenue shows two seasonal peaks — the Oct–Dec festive/wedding season and a smaller Jan New Year bump — with a dip in the Feb–Mar off-season shared by all three agencies tracked."),
      new Paragraph({ children: [img("charts/revenue_trend.png", 600, 300)], spacing: { after: 200 } }),

      p("Client base growth has been the more consistent story: active clients climbed nearly every month, even through the Feb revenue dip, suggesting retainer relationships are holding even when new-project revenue softens."),
      new Paragraph({ children: [img("charts/active_clients.png", 600, 267)], spacing: { after: 200 } }),

      h1("Competitive Benchmark"),
      p("SocialSprout sits in the middle of the three-agency set on revenue and market share — well ahead of the budget competitor, still trailing the established leader."),
      new Paragraph({ children: [img("charts/market_share.png", 380, 317)], alignment: AlignmentType.CENTER, spacing: { after: 200 } }),

      p("On acquisition efficiency, SocialSprout outperforms ViralNest Media by a wide margin, though trails Boostly Creators — likely because Boostly's smaller, cheaper client base is easier to acquire efficiently at low volume."),
      new Paragraph({ children: [img("charts/acquisition_efficiency.png", 500, 321)], spacing: { after: 200 } }),

      new Paragraph({ children: [new PageBreak()] }),

      h1("Service Mix"),
      p("Reels Production and Influencer Collabs together make up 61% of client billings — the core of the business. Content Strategy and Community Management remain small, which may reflect genuine low demand or simply that they aren't being actively pitched alongside the higher-visibility services."),
      new Paragraph({ children: [img("charts/service_mix.png", 600, 337)], spacing: { after: 200 } }),

      h1("What's Driving the Gap"),
      bullet("Acquisition reach, not conversion quality — SocialSprout wins on efficiency but loses on raw spend, so more revenue is available simply by scaling the current playbook rather than fixing it."),
      bullet("Underleveraged service lines — Content Strategy and Community Management sit under 20% combined; these pair naturally with Reels/Influencer work and may be under-attached in proposals."),
      bullet("Seasonal concentration — nearly 40% of tracked revenue lands in the Oct–Dec window; the Feb–Mar dip is a good target for a retainer-focused push since client count holds steady even when project revenue softens."),

      h1("Recommended Action Plan"),
      new Table({
        width: { size: 9600, type: WidthType.DXA },
        columnWidths: [1200, 4800, 1800, 1800],
        rows: [
          actionRow("Step", "Action", "Owner", "Timeframe", true),
          actionRow("1", "Increase client-acquisition spend in a controlled test (e.g. targeted outreach to Bangalore F&B/D2C brands) while tracking cost-per-client against the current ₹12.89 efficiency baseline.", "Owner / Growth", "Next 30 days"),
          actionRow("2", "Bundle Content Strategy as a default add-on for every new Reels/Influencer proposal to raise attach rate.", "Sales", "Next 30 days"),
          actionRow("3", "Build a Feb–Mar retainer push (e.g. discounted 3-month lock-in) to smooth the seasonal revenue dip using the existing stable client base.", "Owner", "Next 60 days"),
          actionRow("4", "Re-run this analysis quarterly to confirm whether the acquisition test is closing the market-share gap.", "Owner", "Ongoing"),
        ],
      }),

      new Paragraph({ spacing: { before: 300 }, children: [] }),
      p("Methodology note: figures are illustrative and generated for demonstration purposes. A client engagement would use the agency's actual invoicing/accounting exports, ad platform spend data, and publicly available competitor signals (Instagram follower/engagement trends, job postings, client testimonials) in place of synthetic data.", { italics: true, color: MUTED, size: 18 }),
    ],
  }],
});

Packer.toBuffer(doc).then((buf) => {
  fs.writeFileSync("SocialSprout_Performance_Analysis.docx", buf);
  console.log("Report written.");
});
