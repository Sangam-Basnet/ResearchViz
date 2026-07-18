import Link from "next/link";

type ButtonProps = {
  children: React.ReactNode;
  href?: string;
  variant?: "primary" | "secondary";
};

export default function Button({
  children,
  href,
  variant = "primary",
}: ButtonProps) {
  const classes =
    variant === "primary"
      ? "rounded-xl bg-blue-600 px-7 py-4 font-medium text-white transition hover:bg-blue-700"
      : "rounded-xl border border-gray-300 px-7 py-4 font-medium text-gray-700 transition hover:border-blue-600 hover:text-blue-600";

  if (href) {
    return (
      <Link href={href} className={classes}>
        {children}
      </Link>
    );
  }

  return <button className={classes}>{children}</button>;
}