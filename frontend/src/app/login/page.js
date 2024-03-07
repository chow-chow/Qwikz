import {
	Card,
	CardContent,
	CardDescription,
	CardFooter,
	CardHeader,
	CardTitle,
} from '@/components/ui/card'
import { Button } from '@/components/ui/button'
import LoginForm from '@/components/login-form'
import Link from 'next/link'

export default function Login() {
	return (
		<section className='flex-1 flex'>
			<div className='container mx-auto mt-4 flex justify-center items-center'>
				<Card className='w-[400px]'>
					<CardHeader>
						<CardTitle>Login</CardTitle>
						<CardDescription>
							Enter your email and password to login
						</CardDescription>
					</CardHeader>
					<CardContent>
						<LoginForm />
					</CardContent>
					<CardFooter className='flex justify-center'>
						<Button asChild variant='link'>
							<Link href={'/signup'}>Don't have an account?</Link>
						</Button>
					</CardFooter>
				</Card>
			</div>
		</section>
	)
}
